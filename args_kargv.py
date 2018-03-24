

# https://eastlakeside.gitbooks.io/interpy-zh/content/args_kwargs/Usage_args.html
# *args 和 **kwargs

def get_name(**kargs):

	for key, val in kargs.items():
		print(key,val)


def parse_args(*args):

	for val in args:
		print(val)



get_name(name="iwang")


parse_args("iwang","mike")