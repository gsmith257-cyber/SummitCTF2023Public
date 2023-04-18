# Ruby dockerfile

FROM ruby:3.0.0

# Install node
RUN apt-get update
RUN apt-get install -y nodejs npm

WORKDIR /app
COPY . /app/

# npm install
RUN npm install

# Get rake dependencies
RUN bundle install

# Run rails server
CMD ["rails", "server", "-b", "0.0.0.0"]