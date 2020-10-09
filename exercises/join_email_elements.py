# Join the tuple's elements so that you get a proper email address.
values = ('mark.hoggins', 'email.com')
type(values)

sep='@'
val=sep.join(values)
print(val)

def mail(values):
    return '@'.join(values)
print(mail(values))