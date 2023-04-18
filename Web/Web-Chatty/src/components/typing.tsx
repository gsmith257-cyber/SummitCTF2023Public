import React from 'react';
import { Box, keyframes, Typography } from '@mui/material';
import { grey } from '@mui/material/colors';

const bubbleOne = keyframes`
0% {}
10% {}
20% {}
30% {
    transform: translateY(-10px);
}
40% {}
50% {
    transform: translateY(-5px);
}
60% {}
70% {
    transform: translateY(0);
}
80% {}
90% {}
100% {}
`

const bubbleTwo = keyframes`
0% {}
10% {}
20% {}
30% {}
40% {
    transform: translateY(-10px);
}
50% {}
60% {
    transform: translateY(-5px);
}
70% {}
80% {
    transform: translateY(0);
}
90% {}
100% {}
`

const bubbleThree = keyframes`
0% {}
10% {}
20% {}
30% {}
40% {}
50% {
    transform: translateY(-10px);
}
60% {}
70% {
    transform: translateY(-5px);
}
80% {}
90% {
    transform: translateY(0);
}
100% {}
`

export default function TypingAnimation() {
    return (
        <Box
            sx={{ marginBottom: 1 }}
            display="flex"
            justifyContent={'flex-start'}
        >
            <Box
                sx={{ borderRadius: '8px', padding: 2, backgroundColor: grey[100] }}
            >
                <Box
                    sx={{
                        display: 'inline-block',
                        width: '10px',
                        height: '10px',
                        borderRadius: '50%',
                        backgroundColor: (theme) => grey[600],
                        animation: (theme) => `${bubbleOne} 0.8s ease-in-out infinite`,
                        animationFillMode: 'both',
                        marginRight: (theme) => theme.spacing(1),
                    }}
                ></Box>
                <Box
                    sx={{
                        display: 'inline-block',
                        width: '10px',
                        height: '10px',
                        borderRadius: '50%',
                        backgroundColor: (theme) => grey[600],
                        animationFillMode: 'both',
                        marginRight: (theme) => theme.spacing(1),
                        animation: (theme) => `${bubbleTwo} 0.8s ease-in-out infinite`,
                    }}
                ></Box>
                <Box
                    sx={{
                        display: 'inline-block',
                        width: '10px',
                        height: '10px',
                        borderRadius: '50%',
                        backgroundColor: (theme) => grey[600],
                        animationFillMode: 'both',
                        animation: (theme) => `${bubbleThree} 0.8s ease-in-out infinite`,
                    }}
                ></Box>
            </Box>
        </Box>
    );
};
