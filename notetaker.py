import argparse

parser = argparse.ArgumentParser(description="add notes to PostgreSQL database")
# group = parser.add_mutually_exclusive_group()
# group.add_argument("-v", "--verbose", action="store_true")
# group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("action", help="what action you'd like to take", choices=['list','create'],default='list',)
args = parser.parse_args()

user_action = args.action

if user_action=='list':
    print("now showing: your notes!")
elif user_action=='create':
    title = input('Please provide the title of your new note: ')
    content = input('Please provide the content: ')
    print(f"""Note saved! 
Title: {title}
Content: {content}    
    """)
