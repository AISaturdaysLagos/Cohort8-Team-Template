# Use the official Node.js image as the base image
FROM node:16 as build

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to install dependencies
COPY package*.json ./

# Install dependencies
RUN yarn

# Copy the rest of the application code
COPY . .

# Build the Vue app for production
RUN yarn build

# Use a smaller, optimized image for serving the app
FROM nginx:alpine

# Copy the built app from the previous stage
COPY --from=build /app/dist /usr/share/nginx/html

# Expose the port that Nginx will run on
EXPOSE 80

# Command to start Nginx
CMD ["nginx", "-g", "daemon off;"]
