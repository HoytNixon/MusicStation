from app import app,db
from app.models import User, Radio, Tag, Message

@app.shell_context_processor
def make_shell_context():
	return {'db':db, 'User':User, 'Radio':Radio, 'Tag':Tag, 'Message':Message}

if __name__ == '__main__':
	app.run()