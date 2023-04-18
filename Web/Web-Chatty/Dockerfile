FROM node:16

# Create app directory
WORKDIR /app

# Copy files
COPY . /app/

# Install dependencies
RUN npm install

# Build app
RUN npm run build

# Expose port
EXPOSE 3000

# Set environment variable OPENAI_API_KEY TODO
ENV OPENAI_API_KEY=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
ENV RECAPTCHA_SECRET_KEY=6LfaV44lAAAAAMKpqheGs-1ARGaDCdHt5tNFbUU5

# Run app
CMD [ "npm", "start" ]
