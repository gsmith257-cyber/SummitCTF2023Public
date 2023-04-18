// components/MessageBubble.tsx
import React from 'react';
import { Box, Typography } from '@mui/material';
import { Theme } from '@mui/system';
import { blue, grey } from '@mui/material/colors';

interface MessageBubbleProps {
    text: string;
    sent: boolean;
}

export default function MessageBubble({ text, sent }: MessageBubbleProps) {
    return (
        <Box
            sx={{ marginBottom: 1 }}
            display="flex"
            justifyContent={sent ? 'flex-end' : 'flex-start'}
        >
            <Box
                sx={{ borderRadius: '8px', padding: 2, maxWidth: '60%', wordWrap: 'break-road', backgroundColor: sent ? blue[300] : grey[100], color: sent ? 'white' : 'black' }}
            >
                <Typography variant="body1">{text}</Typography>
            </Box>
        </Box>
    );
};


// const useStyles = makeStyles((theme: Theme) => ({
//     bubbleContainer: {
//         marginBottom: theme.spacing(1),
//     },
//     bubble: {
//         borderRadius: '1.5rem',
//         padding: theme.spacing(1, 2),
//         maxWidth: '60%',
//         wordWrap: 'break-word',
//     },
//     sent: {
//         background: theme.palette.primary.light,
//         color: theme.palette.primary.contrastText,
//     },
//     received: {
//         background: theme.palette.grey[200],
//         color: theme.palette.text.primary,
//     },
// }));
