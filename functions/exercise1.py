def make_shirt(size, text):
	print(f'This {size}-sized shirt reads "{text}".')

make_shirt('medium', 'winner')

def make_lg_shirt(size = 'large', text = 'I love Python'):
	print(f'This {size}-sized shirt reads "{text}".')

make_lg_shirt()
make_lg_shirt('medium')
make_lg_shirt('small', 'hippo!')
