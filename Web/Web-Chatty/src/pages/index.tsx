import { Box, Grid, Typography } from '@mui/material'
import Chat from '@/components/chat'
import Head from 'next/head'
import NavMenu from '@/components/menu'
import { Stack } from '@mui/system'
import Image from 'next/image';
import FoodBoxLogo from '../../public/assets/logo.png'
import { GoogleReCaptchaProvider } from 'react-google-recaptcha-v3'

export default function Home() {
  return (
    <>
      <Head>
        <title>FoodBox Support</title>
      </Head>
      <Box display='flex' flexDirection='column'>
        <NavMenu />
        <Box
          height='100%'
          maxWidth='md'
          p={4}
          flexGrow={1}
          sx={{ margin: '0 auto' }}>
          <Stack spacing={2}>
            <Typography variant='h3'>
              Chat Support
            </Typography>
            <Typography>
              At FoodBox, our customer support team is second to none. They're the cream of the crop, the cherry on top, and the sprinkles on your ice cream sundae.
            </Typography>

            <Typography>
              Our team is made up of food enthusiasts who know everything there is to know about our products. They're available 24/7 to answer any questions you have, whether you're wondering about the ingredients in our dishes or need help placing an order.
            </Typography>

            <Typography>
              And let's talk about our response time. We don't mess around when it comes to customer support. Our agents can type faster than a hummingbird's wings, and they're always ready to spring into action.
            </Typography>

            <Typography>
              But don't take our word for it. Here's what some of our satisfied customers have to say:
            </Typography>

            <Typography>
              "I had a question about one of the items on the menu, and the FoodBox team was so helpful! They answered my question quickly and made some great suggestions for other dishes I might like." - Sarah M.
            </Typography>

            <Typography>
              "I accidentally placed the wrong order, but the FoodBox team was able to help me fix it in no time. They were so friendly and patient, even though I was a bit frazzled." - John T.
            </Typography>

            <Typography>
              So what are you waiting for? Give our customer support team a try and see for yourself why we're the best in the biz.
            </Typography>
            <GoogleReCaptchaProvider
              reCaptchaKey="6LfaV44lAAAAAFaqSeRt8h6PfaFfHz4Bpo6Wl9lK"
              useEnterprise={false}
              scriptProps={{
                async: false, // optional, default to false,
                defer: false, // optional, default to false
                appendTo: 'head', // optional, default to "head", can be "head" or "body",
                nonce: undefined // optional, default undefined
              }}
            >
              <Chat />
            </GoogleReCaptchaProvider>
          </Stack>
        </Box>

      </Box>
    </>
  )
}
