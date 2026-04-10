Idade_Usuário = int(input("Digite idade"))
Nota = float(input("Digite nota"))
presença = int(input("Digite a frequencia escolar"))

Total_aulas = 200
Frequência_Escolar = (presença / 100) * 200

if Idade_Usuário < 18:
    print("mátricula negada automáticamente.")
elif Idade_Usuário < 18 and Nota < 6 and Frequência_Escolar < 75:  
    print("Matrícula Negada.")
elif Nota >= 9:
    print("Matrícula aprovada automaticamente.")
elif Idade_Usuário >= 18 and Nota >= 6 and Frequência_Escolar >= 75:
    print("Matrícula Aprovada.")
else:
    print("Mátricula negada.")