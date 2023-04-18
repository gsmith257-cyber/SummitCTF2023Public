import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import FoodBoxLogo from '../../public/assets/logo.png'
import Image from 'next/image';
import { Stack } from '@mui/material';

export default function NavMenu() {
    return (
        <Box sx={{ flexGrow: 1 }}>
            <AppBar position="static">
                <Toolbar>
                    <Box marginRight={4} padding={1}>
                        <Image src={FoodBoxLogo} alt='logo' width={64} height={64} />
                    </Box>
                    <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                        FoodBox Inc. Press Release
                    </Typography>
                </Toolbar>
            </AppBar>
        </Box>
    );
}