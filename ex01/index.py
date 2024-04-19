def validate(cpf_param: str):
  CPF = cpf_param.replace(".", "").replace("-", "")
  
  if (CPF.isdigit() and len(CPF) == 11):
    return CPF
  
  return None

def separator(cpf_param: str, limit: int) -> list[int]:
  cpf_list = []

  for index, value in enumerate(cpf_param):
    cpf_list.append(int(value))
    
    if (index == limit):
      return cpf_list
    
def calculate(cpf_param: str):
  first_list = {
    "count": 10,
    "accumulator": 0,
    "list": separator(cpf_param, 8)
  }

  last_list = {
    "count": 11,
    "accumulator": 0,
    "list": separator(cpf_param, 9)
  }

  for digit in enumerate(first_list["list"]):
    first_list["accumulator"] += digit[1] * first_list["count"]
    first_list["count"] -= 1

  for digit in enumerate(last_list["list"]):
    last_list["accumulator"] += digit[1] * last_list["count"]
    last_list["count"] -= 1
  
  first_list["accumulator"] = (first_list["accumulator"] * 10) % 11
  last_list["accumulator"] = (last_list["accumulator"] * 10) % 11

  return [first_list["accumulator"], last_list["accumulator"]]

def execute():
  cpf_input = input("Informe o cpf: ")
  cpf_validated = validate(cpf_input)
  
  if(cpf_validated):
    result = calculate(cpf_validated)
    print(f'Cpf é válido! \nPrimeiro dígito: {result[0]} \nSegundo dígito: {result[1]}')
  else:
    print("Insira um cpf válido!")


execute()