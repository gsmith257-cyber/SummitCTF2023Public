// components/Chat.tsx
import React, { useCallback, useState } from 'react';
import { Box, IconButton, Container, Grid, Paper, TextField, Typography, SvgIcon, Stack } from '@mui/material';
import SendIcon from '@mui/icons-material/Quickreply';
import MessageBubble from './message-bubble';
import TypingAnimation from './typing';
import { Message } from '@/pages/api/chat';
import { useGoogleReCaptcha } from 'react-google-recaptcha-v3';

export default function Chat() {
    const { executeRecaptcha } = useGoogleReCaptcha();

    const [messages, setMessages] = useState<Message[]>([{
        id: 0,
        text: "Welcome to FoodBox customer support! This is Robert speaking. With whom do I have the pleasure of speaking?",
        sent: false,
        captcha: ""
    }]);
    const [input, setInput] = useState('');
    const [waiting, setWaiting] = useState(false);

    const handleSend = async () => {
        if (input.trim() == "") {
            return
        }

        if (!executeRecaptcha) {
            return
        }

        const token = await executeRecaptcha('chat');

        const newMessage: Message = {
            id: messages.length,
            text: input,
            sent: true,
            captcha: token
        };

        const newArray = [newMessage, ...messages]

        setMessages(newArray);

        setInput('');
        setWaiting(true);


        /* Upload and wait for response */
        const toBeUploaded = newArray.slice().reverse()

        try {
            const response = await fetch("/api/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(toBeUploaded),
            });

            if (!response.ok) {
                throw new Error(`HTTP error ${response.status}: ${await response.text()}`);
            }

            const responseData = await response.json() as string;
            console.log("Response data:", responseData);
            toBeUploaded.push({
                id: toBeUploaded.length,
                text: responseData,
                sent: false,
                captcha: ""
            })

            toBeUploaded.reverse()

            setMessages(toBeUploaded)
            setWaiting(false)
        } catch (error) {
            console.error("Error posting chat data:", error);
        } finally {
            setWaiting(false)
        }
    };

    return (
        <Container>
            <Stack spacing={2}>
                <Typography variant='h6'>Your Agent: Rob Ott</Typography>
                <Paper elevation={3}>
                    <Grid container direction="column" spacing={0} p={2}>
                        <Grid item>
                            <Box height={'400px'} overflow='scroll' display={'flex'} flexDirection='column-reverse'>
                                {waiting && <TypingAnimation />}
                                {messages.map((message) => (
                                    <MessageBubble key={message.id} text={message.text} sent={message.sent} />
                                ))}
                            </Box>
                        </Grid>
                        <Grid item>
                            <Box>
                                <Grid container justifyContent="space-between" alignItems="center">
                                    <Grid item xs={11}>
                                        <TextField
                                            placeholder='Send a message to our expert support team'
                                            fullWidth
                                            value={input}
                                            onChange={(e) => setInput(e.target.value)}
                                            disabled={waiting}
                                            onKeyDown={(e) => {
                                                if (e.key === 'Enter' && !waiting) {
                                                    handleSend();
                                                }
                                            }}
                                        />
                                    </Grid>
                                    <Grid item xs={1} textAlign='center'>
                                        <IconButton onClick={handleSend} disabled={waiting}>
                                            <SvgIcon color={waiting ? 'disabled' : 'primary'}>
                                                <SendIcon />
                                            </SvgIcon>
                                        </IconButton>
                                    </Grid>
                                </Grid>
                            </Box>
                        </Grid>
                    </Grid>
                </Paper>
            </Stack>
        </Container>
    );
}