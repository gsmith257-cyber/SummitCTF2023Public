import * as React from 'react'

// Import chakra components
import { ChakraProvider, Stack, Center, Heading, FormControl, Input, Button, FormLabel, Box, Text, FormHelperText, Alert, AlertIcon, Tabs, TabList, TabPanels, Tab, TabPanel, Code } from '@chakra-ui/react'

// Import ReactQuill
import ReactQuill from 'react-quill'
import 'react-quill/dist/quill.snow.css';


function Receipt () {

  /* Define states */
  const [business, setBusiness] = React.useState('');
  const [name, setName] = React.useState('');
  const [email, setEmail] = React.useState('');
  const [errorMessage, setErrorMessage] = React.useState('');
  const [price, setPrice] = React.useState('');
  const [comments, setComments] = React.useState('');
  const [addressLineOne, setAddressLineOne] = React.useState('');
  const [addressLineTwo, setAddressLineTwo] = React.useState('');
  const [item, setItem] = React.useState('');
  const [fees, setFees] = React.useState('');
  const [method, setMethod] = React.useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    if (business === '' || name === '' || email === '' || price === '' || addressLineOne === '' || addressLineTwo === '' || item === '' || method === '') {
      setErrorMessage('Please fill out all fields, you dingus.');
      return;
    }

    /* Ensure that prices and fees are monetary values */
    if (isNaN(price) || isNaN(fees)) {
      setErrorMessage('Please enter a valid monetary value for prices and fees, you dingus.');
      return;
    }

    setErrorMessage('');

    /* Send data to server including CSRF token */
    fetch('/api/receipt', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRF-Token': document.querySelector('meta[name="csrf-token"]').getAttribute('content')
      },
      body: JSON.stringify({
        business,
        name,
        email,
        price,
        comments,
        addressLineOne,
        addressLineTwo,
        item,
        fees,
        method
      })
    }).then(response => {
      if (response.status === 200) {
        /* Display PDF data in browser */
        response.blob().then(blob => {
          const url = window.URL.createObjectURL(blob);
          const a = document.createElement('a');
          a.href = url;
          a.download = 'receipt.pdf';
          a.click();
        });
      }
    });
  }
  // 2. Wrap ChakraProvider at the root of your app
  return (
    <ChakraProvider>
      <Tabs variant='soft-rounded'>
        <Stack spacing={8}>
          <Box p={6}>
            <TabList>
              <Tab>Home</Tab>
              <Tab>About</Tab>
            </TabList>
          </Box>
        </Stack>
        <Stack spacing={8} mx='auto' p={6} maxW='md' textAlign='center'>
          <Center>
            <Box maxW='md'>
              <Heading>Receipt Buddy</Heading>
              <Text>
                The easiest and most secure way to generate professional-looking invoices in a matter of minutes.
              </Text>
            </Box>
          </Center>
        </Stack>
        <Stack>
          <TabPanels>
            <TabPanel>
              <Center>
                <Box maxW='lg' rounded='lg' boxShadow='lg' p={8}>
                  <Stack spacing={4}>
                    {errorMessage != '' && <Alert status='error' variant='subtle'>
                      <AlertIcon />
                      {errorMessage}
                    </Alert>}

                    <FormControl isRequired>
                      <FormLabel htmlFor='business'>Business</FormLabel>
                      <Input placeholder='Acme Inc.' id = 'business' onChange={(e) => setBusiness(e.target.value)} />
                      <FormHelperText>The name of your business</FormHelperText>
                    </FormControl>

                    <FormControl isRequired>
                      <FormLabel htmlFor='address_line_one'>Address line 1</FormLabel>
                      <Input placeholder='1600 Pennsylvania Avenue NW' id = 'address_line_one' onChange={(e) => setAddressLineOne(e.target.value)} />
                      <FormHelperText>Business address line</FormHelperText>
                    </FormControl>

                    <FormControl isRequired>
                      <FormLabel htmlFor='address_line_two'>Address line 2</FormLabel>
                      <Input placeholder='Washington, DC 20500' id = 'address_line_two' onChange={(e) => setAddressLineTwo(e.target.value)} />
                      <FormHelperText>Business address line</FormHelperText>
                    </FormControl>

                    <FormControl isRequired>
                      <FormLabel htmlFor='name'>Customer name</FormLabel>
                      <Input placeholder='Jane Smith' id = 'name' onChange={(e) => setName(e.target.value)} />
                    </FormControl>

                    <FormControl isRequired>
                      <FormLabel htmlFor='email'>Customer email</FormLabel>
                      <Input placeholder='jsmith@gmail.com' id = 'email' onChange={(e) => setEmail(e.target.value)} />
                    </FormControl>

                    <FormControl isRequired>
                      <FormLabel htmlFor='item'>Item</FormLabel>
                      <Input placeholder='Widgets' id = 'item' onChange={(e) => setItem(e.target.value)} />
                      <FormHelperText>What you're charging for</FormHelperText>
                    </FormControl>

                    <FormControl isRequired>
                      <FormLabel htmlFor='price'>Price</FormLabel>
                      <Input placeholder='$9.99' id = 'price' onChange={(e) => setPrice(e.target.value)} />
                    </FormControl>

                    <FormControl>
                      <FormLabel htmlFor='fees'>Fees</FormLabel>
                      <Input placeholder='$1.23' id = 'fees' onChange={(e) => setFees(e.target.value)} />
                      <FormHelperText>Set any additional taxes or fees</FormHelperText>
                    </FormControl>

                    <FormControl isRequired>
                      <FormLabel htmlFor='method'>Payment method</FormLabel>
                      <Input placeholder='Cash' id = 'method' onChange={(e) => setMethod(e.target.value)} />
                    </FormControl>

                    <FormControl>
                      <FormLabel htmlFor='comments'>Comments</FormLabel>
                      <ReactQuill theme='snow' id='comments' onChange={setComments} />
                    </FormControl>

                    <Button onClick={handleSubmit}>
                      Generate receipt
                    </Button>
                  </Stack>
                </Box>
              </Center>
            </TabPanel>
            <TabPanel>
              <Center>
                <Box maxW='lg' rounded='lg' boxShadow='lg' p={4}>
                  <Heading fontSize={'md'}>WHO WE ARE</Heading>
                  <Text mb={8}>Receipt Buddy is a receipt aggregation company. We live receipts. We breath receipts. We eat receipts. With millions of receipts being generated every hour, we know what we're talking about.</Text>
                
                  <Heading fontSize={'md'}>THE COST OF OUR PRODUCT</Heading>
                  <Text mb={8}>Receipt Buddy will always be free. Even after hell freezes over. Even after the end of the universe. You can always count on that.</Text>
                
                  <Heading fontSize={'md'}>YOUR PRIVACY</Heading>
                  <Text mb={8}>Receipt Buddy takes data privacy seriously. That's why we only sell your receipt data to reputable companies with a proven track records for privacy, such as Facebook.</Text>
                
                  <Heading fontSize={'md'}>SECURITY</Heading>
                  <Text mb={8}>Receipt Buddy takes security seriously. Our incident response policy is to unplug the ethernet cable from our server. We also protect our ports with latex condoms to prevent security breaches. This is to protect our proprietary information located at <Code colorScheme='red' children="/app/app/controllers/receipt_controller.rb" />.</Text>

                  <Heading fontSize={'md'}>TECHNOLOGY</Heading>
                  <Text mb={8}>Receipt Buddy uses bleeding edge technologies, such as Ruby on Rails, the magnetron from our kitchen's microwave, wicked_pdf, five bananas, React, and two cups attached to a string.</Text>

                  <Heading fontSize={'md'}>RESPONSIBLE DISCLOSURE</Heading>
                  <Text>Please don't hack us. And if you do, we will do everything in our power to make your life as miserable as possible. At Receipt Buddy, we know where you live. We know where everyone lives.</Text>
                </Box>
              </Center>
            </TabPanel>
          </TabPanels>
        </Stack>
      </Tabs>
    </ChakraProvider>
  )
}

export default Receipt