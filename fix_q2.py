import json

q = json.load(open('questions_2.json', encoding='utf-8'))
t2 = q['2']

# Manually fix all questions with OCR issues
fixes = {
    '52': {
        'q': 'What does the woman offer to do?',
        'o': ['Pass out the report at the meeting.', 'Make copies of the report.', "Clean the man's desk.", 'Work until 8:00.']
    },
    '53': {
        'q': 'How many nights does the man want to stay at the hotel?',
        'o': ['1.', '2.', '3.', '4.']
    },
    '60': {
        'q': 'How far does he have to go?',
        'o': ['1 block.', '3 blocks.', '1 mile.', '3 miles.']
    },
    '61': {
        'q': 'How much will he have to pay?',
        'o': ['$0.', '$4.', '$8.', '$20.']
    },
    '62': {
        'q': 'How does the woman feel?',
        'o': ['Sad.', 'Bored.', 'Happy.', 'Angry.']
    },
    '63': {
        'q': "When will they celebrate the man's promotion?",
        'o': ['Now.', 'Tonight.', 'At 10:00.', 'Next Monday.']
    },
    '64': {
        'q': 'What does the woman offer to do?',
        'o': ['Help the man with his work.', 'Prepare dinner for the man.', "Pay for the man's lunch.", 'Give the man her seat.']
    },
    '65': {
        'q': 'Why is the woman hosting the dinner?',
        'o': ["She's having a meeting.", "She's entertaining clients.", "She's having a birthday party.", "She's celebrating her retirement."]
    },
    '66': {
        'q': 'How many people will be at the dinner?',
        'o': ['15.', '16.', '50.', '60.']
    },
    '67': {
        'q': 'What food does the woman order?',
        'o': ['Rice.', 'Fish.', 'Steak.', 'Chicken.']
    },
    '68': {
        'q': 'What is the occasion?',
        'o': ['A trip.', 'A party.', 'A present.', 'An interview.']
    },
    '69': {
        'q': 'What color shoes does the woman want?',
        'o': ['White.', 'Gray.', 'Blue.', 'Black.']
    },
    '70': {
        'q': 'When does she need to wear them?',
        'o': ['Now.', 'Sunday.', 'Monday.', 'Next month.']
    },
    '77': {
        'q': 'Who is this talk for?',
        'o': ['Office workers.', 'Police officers.', 'Health experts.', 'Gym teachers.']
    },
    '80': {
        'q': "What kind of business is Branwell's?",
        'o': ['Cafe.', 'Sports store.', 'Clothing store.', 'Travel agency.']
    },
    '81': {
        'q': 'What size discount is offered?',
        'o': ['5%.', '10%.', '20%.', '25%.']
    },
    '82': {
        'q': 'When does the sale begin?',
        'o': ['Saturday.', 'Sunday.', 'Monday.', 'Tuesday.']
    },
    '83': {
        'q': 'What kind of business is advertised?',
        'o': ['Employment agency.', 'Computer training.', 'Office rental.', 'Hotel.']
    },
    '84': {
        'q': 'What fee is charged for the service?',
        'o': ['$0.', '$13.', '$30.', '$35.']
    },
    '85': {
        'q': 'What are listeners asked to do?',
        'o': ['Write a letter.', 'Call the office.', 'Visit the office.', 'Make an appointment.']
    },
    '86': {
        'q': 'What is the weather like now?',
        'o': ['Cold.', 'Windy.', 'Rainy.', 'Snowy.']
    },
    '87': {
        'q': 'What problem has the weather caused?',
        'o': ['School closings.', 'Trains delayed.', 'Loss of electricity.', 'Damage to bridge.']
    },
    '88': {
        'q': 'When will the weather change?',
        'o': ['This afternoon.', 'This evening.', 'Tomorrow morning.', 'Next week.']
    },
    '89': {
        'q': 'When does the conference start?',
        'o': ['2:00.', '10:00.', '10:15.', '12:15.']
    },
    '90': {
        'q': 'Where will lunch be served?',
        'o': ['In the lobby.', 'In the auditorium.', 'On the ground floor.', 'On the second floor.']
    },
    '91': {
        'q': 'What will happen after lunch?',
        'o': ['Coffee will be served.', 'There will be a discussion.', 'Workshops will be held.', 'Registration will end.']
    },
    '100': {
        'q': 'What are the listeners asked to do?',
        'o': ['Attend a lunch.', 'Pay with a check.', 'Mark their calendars.', 'Go to a press conference.']
    },
    '44': {
        'q': 'Where does this conversation take place?',
        'o': ['A bank.', "An accountant's office.", 'A driving school.', 'An office supply store.']
    },
    '57': {
        'q': "What's the weather like?",
        'o': ['Rain.', 'Snow.', 'Hot.', 'Clear.']
    },
    '71': {
        'q': 'How is the man traveling?',
        'o': ['On a bus.', 'On a plane.', 'On a train.', 'On a ship.']
    }
}

for qnum, data in fixes.items():
    if qnum in t2:
        t2[qnum]['q'] = data['q']
        t2[qnum]['o'] = data['o']

# Verify all have 4 options
problems = []
for qnum in range(41, 101):
    q_data = t2.get(str(qnum), {})
    opts = q_data.get('o', [])
    if len(opts) != 4:
        problems.append(f'Q{qnum}: {len(opts)} opts -> {opts}')

if problems:
    for p in problems:
        print('PROBLEM:', p)
else:
    print('All Q41-100 have 4 options. OK!')

with open('questions_2.json', 'w', encoding='utf-8') as f:
    json.dump(q, f, ensure_ascii=False, indent=2)
print('Saved questions_2.json')
