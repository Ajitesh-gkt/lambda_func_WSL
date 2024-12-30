# Lambda Function in WSL

This repository contains a sample AWS Lambda function developed and tested within the Windows Subsystem for Linux (WSL) environment.

## Prerequisites

Before you begin, ensure you have the following installed:

- **WSL**: Windows Subsystem for Linux installed on your Windows machine.
- **AWS CLI**: Amazon Web Services Command Line Interface for managing AWS resources.
- **AWS SAM CLI**: AWS Serverless Application Model Command Line Interface for building and deploying serverless applications.
- **Docker**: For building and testing Lambda functions locally.

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Ajitesh-gkt/lambda_func_WSL.git
   cd lambda_func_WSL
   ```

2. **Build the Lambda Function**:

   Use the AWS SAM CLI to build the function:

   ```bash
   sam build
   ```

3. **Test Locally**:

   Invoke the function locally using the SAM CLI:

   ```bash
   sam local invoke
   ```

4. **Deploy to AWS**:

   Deploy the function to your AWS account:

   ```bash
   sam deploy --guided
   ```

   Follow the prompts to set up your deployment configuration.

## Project Structure

The repository is organized as follows:

```
lambda_func_WSL/
├── README.md           # Project documentation
├── template.yaml       # SAM template for defining the AWS resources
└── src/                # Directory containing the Lambda function code
    └── app.py          # Main application code
```

## Notes

- Ensure your AWS credentials are configured in WSL. You can set them up using `aws configure`.
- The `template.yaml` file defines the AWS resources and their configurations.
- Modify the `app.py` file in the `src` directory to change the function's behavior.

## References

- [AWS SAM CLI Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)
- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/index.html)
- [WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

This template provides a clear overview of your project, setup instructions, and references for users. Feel free to customize it further to suit your project's specific details. 
