def getMessage(text: str):
    message='No Meesage'
    if text.lower()=='/cricketscore':
        message='ENG vs NZ 2021 Highlights, 1st Test, Day 5: Match Ends in a Draw'
    if text.lower()=='/livenews':
        message='Delhi: Covaxin only for 2nd dose beneficiaries in 18-44 age group'
    return message
