def generate_client_code(client_name, db_session, Client):
    # Take first 3 letters of name (uppercase)
    prefix = client_name[:3].upper()
    if len(prefix) < 3:
        prefix += ''.join(chr(65 + i) for i in range(3 - len(prefix)))
    
    # Find existing codes starting with prefix
    existing_codes = db_session.query(Client.client_code)\
        .filter(Client.client_code.like(f"{prefix}%")).all()
    existing_numbers = [int(c[0][3:]) for c in existing_codes if c[0][3:].isdigit()]
    
    next_number = max(existing_numbers, default=0) + 1
    return f"{prefix}{next_number:03d}"
