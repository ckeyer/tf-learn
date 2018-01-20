

dev:
	docker run --rm -it \
	 --name tf-learning \
	 -v `pwd`:/opt/tf \
	 -w /opt/tf \
	 ckeyer/dev:tf-py3 bash