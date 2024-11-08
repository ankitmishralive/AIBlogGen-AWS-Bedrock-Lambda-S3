
import json
import boto3 
import botocore.config 
import responses
from datetime import datetime

def blog_generate_using_bedrock(blogtopic:str)->str:

    prompt = f"""
         <s>Human: Write a 200 words Blog on the topic {blogtopic}
         Assistant: 

    """

    body = {
        "prompt": prompt,
        "max_gen_len": 512,
        "temperature": 0.5,
        "top_p": 1.0,
        # "n": 1
    }

    try:
        bedrock= boto3.client("bedrock-runtime",region_name="ap-south-1",
                              config=botocore.config.Config(read_timeout=300,retries={'max_attempts':3})
        )

        response= bedrock.invoke_model(body=json.dumps(body),modelId="meta.llama3-70b-instruct-v1:0")

        # response_content= response.get('body').read()
        response_content = response['body'].read()
        response_data = json.loads(response_content)

        # response_data =json.loads(response_content)
        print(response_data)
        blog_details = response_data['generation']

        return blog_details
                             

    except Exception as e:
        print(f"Error occurred: {e}")
        return "Error occurred while generating the blog."
    


# blog_generate_using_bedrock(blogtopic="Ankit Mishra")



def save_blog_details_in_S3(s3_key,s3_bucket,generate_blog):

    try:
        s3_client = boto3.client('s3')
        s3_client.put_object(Bucket=s3_bucket, Key=s3_key, Body=generate_blog)
        print(f"Blog details saved successfully in S3 bucket: {s3_bucket} and Key: {s3_key}")
    except Exception as e:
        print(f"Error occurred while saving blog details in S3: {e}")





### Lambda Handler 

def lambda_handler(event, context):
    # TODO implement
    event= json.loads(event['body'])

    blogTopic = event['blogtopic']

    generate_blog = blog_generate_using_bedrock(blogTopic)


    if generate_blog:
        ## Saing Blog in S3 bucket 

        current_time = datetime.now().strftime("%H:%M:%S")
        s3_keys = f"blog-output/{current_time}.txt"

        s3_bucket = "aws_bedrock_v1"

        save_blog_details_in_S3(s3_keys, s3_bucket, generate_blog)

    
    else: 
        print("No Blog was Generated !")

    return {
       'statusCode': 200,
        'body': json.dumps('Blog Generation completed successfully.')
    }




        


   