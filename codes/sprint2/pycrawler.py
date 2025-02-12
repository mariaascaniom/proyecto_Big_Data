import boto3

BUCKET_NAME = "tradingviewdata"
DATABASE_NAME = "trade_data_imat3a05"
CRAWLER_NAME = "tradingviewdata_crawler"
ROLE_NAME = "glue_role"

aws_access_key_id = "" 
aws_secret_access_key = ""
aws_session_token = ""

session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token,
    region_name="eu-south-2"
)
glue_client = session.client("glue")

# Create database 

response = glue_client.create_database(
    DatabaseInput={
        'Name': DATABASE_NAME,
        'Description': 'This database has tradingview data',
    }
)
print("Successfully created database")

# Create crawler

response = glue_client.create_crawler(
    Name=CRAWLER_NAME,
    Role=ROLE_NAME,
    DatabaseName=DATABASE_NAME,
    Targets={
        'S3Targets': [
            {
                'Path': f's3://{BUCKET_NAME}',  
            },

        ]
    },
    RecrawlPolicy={'RecrawlBehavior': 'CRAWL_EVERYTHING'},
    TablePrefix='python_'
)
print("Successfully created crawler")

# Start crawler

try:
    response = glue_client.start_crawler(
        Name=CRAWLER_NAME
    )
    print("Successfully started crawler")
except:
    print("error in starting crawler")

