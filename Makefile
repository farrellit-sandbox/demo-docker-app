test:
	REGION=us-east-2 ExtraENV='Source="",Target="142165916501.dkr.ecr.us-east-2.amazonaws.com/farrellit-demo/webapp"' python ./build.py
	REGION=us-east-2 ExtraENV='Source="142165916501.dkr.ecr.us-east-2.amazonaws.com/farrellit-demo/webapp",Target="142165916501.dkr.ecr.us-east-2.amazonaws.com/farrellit-demo/webapp"' python ./build.py
