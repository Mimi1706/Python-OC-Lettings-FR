Error Monitoring with Sentry
=============================================

To enhance error monitoring and management, Sentry has been integrated into the project.

To configure Sentry for error monitoring in this project, you need to add your Sentry DSN to a .env file. Use the .env.dist file as a template to create your own .env file.

### Steps:

1. **Copy the `.env.dist` file**  
   Duplicate the `.env.dist` file and rename the copy to `.env`. This will serve as your environment file.

   ```bash
   cp .env.dist .env
   ```

2. **Retrieve the Sentry DSN**  

To retrieve your DSN:

- Log in to [Sentry.io](https://sentry.io/) and navigate to your project.
- In the project settings, go to the **Client Keys (DSN)** section.
- Copy your DSN, and update the SENTRY_DSN value in your .env

3. **Trigger an error**  
You can trigger an error to test if Sentry is correctly monitoring the application by accessing the path `/error_500`