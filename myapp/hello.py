import fire

def hello(amount=1):
  tax_price = 17
  tax = (tax_price/100) * amount
  return tax

if __name__ == '__main__':
  fire.Fire(hello)