# End to End A.I Blog Generation with AWS Bedrock, AWS Lambda and S3 Storage

This project is designed to generate a blog using AWS Bedrock's language model service, specifically leveraging Meta's LLama model (meta.llama3-70b-instruct-v1:0). The Overall architecture involves AWS Lambda, API Gateway, Bedrock, S3, and Postman as the API client for testing. 

## Architecture

Below is the architecture diagram for the Blog Generation system:

![Blog Generation Architecture](architecture.png)


- **Postman**: Used to test the API endpoint.
- **API Gateway**: Acts as the entry point, routing requests to the Lambda function.
- **AWS Lambda**: Executes the blog generation logic by invoking the Bedrock model and saves the output to S3.
- **AWS Bedrock**: Provides a large language model (LLM) used to generate the blog content.
- **Amazon S3**: Stores the generated blog as a text file.

## Prerequisites

- **AWS Account**: You need an AWS account to set up and configure the services.
- **AWS CLI**: [AWS CLI](https://aws.amazon.com/cli/) installed and configured.
- **Postman**: For sending test requests to the API.

## Setup

### 1. Configure Bedrock and S3

- **Amazon Bedrock**: Ensure Bedrock is enabled in your AWS account.
- **Amazon S3**: Create an S3 bucket (e.g., `aws_bedrock_v1`) where the generated blog text files will be stored.

### 2. Deploy Lambda Function

1. **Create a Lambda function** in AWS Lambda.
2. **Set up permissions** for the Lambda function:
   - Grant `S3` permissions to store generated blog content.
   - Grant `Bedrock` permissions to call the Bedrock model.
3. Upload the `lambda_function.py` code (below) to the Lambda function, ensuring any dependencies like `botocore` and `boto3` are properly installed.

### 3. Configure API Gateway

1. Set up an **API Gateway** to trigger the Lambda function.
2. Create a **POST** endpoint to handle incoming requests with `blogtopic` as a parameter in the body.
3. Enable **CORS** if testing with Postman.

### 4. Testing with Postman

- Use **Postman** to make a `POST` request to the API Gateway endpoint with JSON body input:
    ```json
    {
      "blogtopic": "Your Blog Topic Here"
    }
    ```



The function will generate a blog, save it to S3, and respond with a confirmation message.

## Troubleshooting

- **Permissions**: Ensure the Lambda function has `S3` write permissions and `Bedrock` invoke permissions.
- **Timeouts**: Adjust the Lambda timeout settings to ensure Bedrock has enough time to generate the blog.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

This project is created and maintained by [Ankit Mishra](https://ankitmishra.live/).

You can find my GitHub profile here: [@ankitmishralive](https://github.com/your-github-id).

