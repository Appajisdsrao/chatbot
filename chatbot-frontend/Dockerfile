# Use the official Node.js 16 image (non-Alpine)
FROM node:16

# Set the working directory
WORKDIR /app

# Install dependencies
COPY package*.json /app/
RUN npm install
RUN npm install crypto-browserify stream-browserify buffer

# Copy all project files
COPY . /app/

# Expose the port the app will run on
EXPOSE 3000

# Start the application in dev mode
CMD ["npm", "run", "dev"]
