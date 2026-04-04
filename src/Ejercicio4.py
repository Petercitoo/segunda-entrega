def ingresar_emails():
    emails = []
    emailing = ""
    while emailing != "termino":
        emailing = input("Ingrese su email\n")
        if(emailing != "termino"):
            emails.append(emailing)
    return emails

def validar_emails(emails):
    for email in emails:
        if (email.count("@") == 1 and
            not email.startswith(("@", ".")) and 
            not email.endswith(("@", "."))):    
            name,domain = email.split("@")  
            if (len(name)>0 and
                domain.count(".")>0 and
                len(domain) > 2):
                print(f"La direccion de email {email} es valida")
        else:
            print(f"La direccion de email {email} es invalida")
