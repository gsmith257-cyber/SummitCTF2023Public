import { Box, Grid, Typography } from '@mui/material'
import Head from 'next/head'
import NavMenu from '@/components/menu'
import { Stack } from '@mui/system'

export default function Home() {
  return (
    <>
      <Head>
        <title>FoodBox Inc. Press Release</title>
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
              Recipe Exclusions Standard
            </Typography>
            <Typography>
              Proposal for a Recipe Exclusions Standard
            </Typography>
            <Typography>
              April 15, 2023
            </Typography>
            <Typography>
              FoodBox is committed to providing its customers with high-quality ingredients and recipes. To ensure customer safety and satisfaction, FoodBox proposes the following Recipe Exclusions Standard (RES) to be followed by all ingredient delivery companies.
            </Typography>
            <Typography>
              1. Allergens:
              All ingredients and recipes must be clearly labeled with any potential allergens, including but not limited to nuts, shellfish, gluten, and dairy. Customers should have the option to exclude allergens from their orders.
            </Typography>
            <Typography>
              2. Dietary Restrictions:
              Recipes should be marked with any dietary restrictions, such as vegetarian, vegan, and low-carb. Customers should have the option to filter recipes based on their dietary needs.
            </Typography>
            <Typography>
              3. Health Concerns:
              Recipes containing ingredients that are known to have adverse health effects should be clearly marked. These ingredients may include high levels of sodium, saturated fats, or added sugars.
            </Typography>
            <Typography>
              4. Religious Restrictions:
              Ingredients and recipes should be labeled to indicate any restrictions based on religious beliefs, such as halal or kosher. Customers should have the option to filter recipes based on their religious restrictions.
            </Typography>
            <Typography>
              5. Cultural Considerations:
              Ingredients and recipes should be marked to indicate cultural considerations. This includes recipes that are specific to certain regions, as well as recipes that may be offensive or inappropriate to certain cultures.
            </Typography>
            <Typography>
              FoodBox believes that the Recipe Exclusions Standard will ensure that ingredient delivery companies are providing their customers with the highest quality ingredients and recipes while also prioritizing customer safety and satisfaction. We hope that other companies will adopt these standards to create a better experience for their customers.
            </Typography>
          </Stack>
        </Box>

      </Box>
    </>
  )
}
