while True:
  print('''    
  ---------------------------------------
  1 - ROI (Retorno sobre o Investimento)
  2 - ROE (Retorno sobre o Patrimônio Líquido)
  3 - ROIC (Retorno sobre o Capital Investido)
  4 - MGBT (Margem Bruta)
  5 - MGL (Margem Líquida)
  6 - EBITDA1 (Lucros antes de juros, impostos, depreciação e amortização) - (EBIT + Depreciação + Amortização)
  7 - EBITDA2 (Lucros antes de juros, impostos, depreciação e amortização) - (Receita Total - Custos e Despesas Operacionais)
  8 - PCT (Participação de capital de terceiros)
  9 - LC (Liquidez Corrente)
  10 - LS (Liquidez Seca)
  11 - LI (Liquidez Imediata) 
  12 - Aprender mais sobre cada opção.
  13- Sair.
  ---------------------------------------
  ''')

  opcao = int(input('Escolha a opção que deseja: '))

  if 1 <= opcao <= 13:
      if opcao == 1:
          ll = float(input('Digite o Lucro Liquido: '))
          ii = float(input('Digite o Investimento Inicial: '))
          roi = (ll/ii)*100
          print(f'ROI = {roi}%.')

      elif opcao ==2:
          ll = float(input('Digite o Lucro Liquido: '))
          plm = float(input('Digite o Patrimônio Líquido médio: '))
          roe = (ll/plm)*100
          print(f'ROE = {roe}%.')

      elif opcao ==3:
          nopat = float(input('Digite o Lucro após Impostos: '))
          ci = float(input('Digite o Capital Investido: '))
          roic = nopat/ci
          print(f'ROIC = {roic}%.')
      
      elif opcao ==4:
          lb = float(input('Digite o Lucro Bruto: '))
          rt = float(input('Digite a Receita Total: '))
          mgbt = (lb/rt)*100
          print(f'MGBT = {mgbt}%.')

      elif opcao ==5:
        ll = float(input('Digite o Lucro Liquido: '))
        rt = float(input('Digite a Receita Total: '))
        mgl = (ll/rt)*100
        print(f'MGL = {mgl}%.')

      elif opcao == 6:
        ebit = float(input('Digite o Lucro antes dos Impostos: '))
        dp = float(input('Digite a Depreciação: '))
        am = float(input('Digite a Amortização: '))
        ebitda1 = ebit + dp + am
        print(f'EBITDA = {ebitda1}.')

      elif opcao ==7:
        rt = float(input('Digite a Receita Total: '))
        cdo = float(input('Digite o total de Custos e Despesas Operacionais: '))
        ebitda2 = rt - cdo
        print(f'EBITDA = {ebitda2}.')

      elif opcao ==8:
        ct = float(input('Digite o Capital de Terceiros Investido: '))
        cti = float(input('Digite o Capital total Investido: '))
        pct = (ct/cti)*100
        print(f'PCT = {pct}%.') 

      elif opcao ==9:
        ac = float(input('Digite os Ativos Circulantes: '))
        pc = float(input('Digite os Passivos Circulantes: '))
        lc = ac/pc
        print(f'LC = {lc}.') 

      elif opcao ==10:
        ac = float(input('Digite os Ativos Circulantes: '))
        est = float(input('Digite o valor dos Estoques: '))
        pc = float(input('Digite os Passivos Circulantes: '))
        ls = (ac-est)/pc
        print(f'LS = {ls}.')

      elif opcao ==11:
        cc = float(input('Digite o Caixa e Equivalentes de Caixa: '))
        pc = float(input('Digite os Passivos Circulantes: '))
        li = cc/pc
        print(f'LI = {li}.')

      elif opcao == 12:
        while True:
          print('''    
    ---------------------------------------
    1 - ROI (Retorno sobre o Investimento)
    2 - ROE (Retorno sobre o Patrimônio Líquido)
    3 - ROIC (Retorno sobre o Capital Investido)
    4 - MGBT (Margem Bruta)
    5 - MGL (Margem Líquida)
    6 - EBITDA (Lucros antes de juros, impostos, depreciação e amortização) (EBIT + Depreciação + Amortização) | (Receita Total - Custos e Despesas Operacionais) 
    7 - PCT (Participação de capital de terceiros)
    8 - LC (Liquidez Corrente)
    9 - LS (Liquidez Seca)
    10 - LI (Liquidez Imediata)
    11 - Voltar ao menu inicial
    ---------------------------------------
    ''')

          opcao_aprender = int(input('Digite o número correspondente a opção que deseja aprender mais: '))

          if 1 <= opcao_aprender <= 11:
              if opcao_aprender == 1:
                  print('''
          O ROI é uma medida útil porque permite comparar a rentabilidade de diferentes investimentos de maneira padronizada.
          Dessa forma, você pode identificar oportunidades mais atraentes e tomar decisões de investimento mais informadas.
          Além disso, o ROI também ajuda a avaliar o desempenho de um investimento ao longo do tempo, possibilitando ajustes na estratégia, caso necessário.
          ROI = (Lucro Líquido / Investimento Inicial) x 100
          ''')
              elif opcao_aprender == 2:
                  print('''
          O ROE é um indicador importante porque reflete a eficiência com que uma empresa utiliza seus recursos próprios pra gerar lucro.
          Um ROE alto indica que a empresa é capaz de gerar mais lucro com menos recursos, o que é um sinal positivo para os investidores.
          Além disso, comparar o ROE de diferentes empresas dentro do mesmo setor pode ajudar a identificar aquelas que estão gerenciando seus recursos de maneira mais eficiente.
          ROE = Lucro Líquido / Patrimônio Líquido Médio''')
              elif opcao_aprender == 3:
                  print('''
          O ROIC é um indicador importante porque ajuda a avaliar a eficiência com que uma empresa utiliza o capital investido, seja ele próprio ou de terceiros.
          Um ROIC alto indica que a empresa é capaz de gerar um retorno maior com os recursos disponíveis, o que pode ser um sinal de boa gestão e um atrativo para os investidores.
          Além disso, comparar o ROIC de diferentes empresas dentro do mesmo setor pode auxiliar na identificação das companhias que estão gerenciando seus recursos de maneira mais eficiente e, assim, têm maior potencial de crescimento.
          ROIC = NOPAT / Capital Investido''')
              elif opcao_aprender == 4:
                  print('''
          A Margem Bruta é importante porque indica a eficiência com que a empresa transforma suas vendas em lucro bruto, ou seja, quanto do valor das vendas sobra após a dedução dos custos diretos de produção.
          Uma Margem Bruta alta sugere que a empresa tem um bom controle sobre seus custos e é capaz de gerar lucro com sua atividade principal.
          Além disso, comparar a Margem Bruta de diferentes empresas dentro do mesmo setor pode auxiliar na identificação das companhias que possuem maior eficiência operacional e vantagem competitiva.
          Margem Bruta = (Lucro Bruto / Receita Total) x 100''')
              elif opcao_aprender == 5:
                  print('''
          A Margem Líquida é importante porque indica a eficiência com que a empresa transforma sua receita em lucro líquido, após considerar todos os custos e despesas, incluindo custos de produção, despesas operacionais, juros e impostos.
          Uma Margem Líquida alta sugere que a empresa tem um bom controle sobre seus custos totais e é capaz de gerar lucro de maneira sustentável.
          Além disso, comparar a Margem Líquida de diferentes empresas dentro do mesmo setor pode ajudar a identificar aquelas que estão gerenciando seus custos de forma mais eficiente e possuem maior potencial de rentabilidade.
          Margem Líquida = (Lucro Líquido / Receita Total) x 100''')
              elif opcao_aprender == 6:
                  print('''
          O EBITDA é importante porque permite avaliar a capacidade de geração de caixa operacional de uma empresa, independentemente da sua estrutura de capital e das decisões de investimento de longo prazo.
          Essa medida é especialmente útil para comparar empresas dentro do mesmo setor, já que pode eliminar diferenças decorrentes de políticas de financiamento e de depreciação.
          Além disso, o EBITDA pode ser um indicativo de liquidez e solidez financeira da empresa, uma vez que reflete a capacidade de gerar recursos para pagar dívidas e financiar investimentos.
          EBITDA = EBIT + Depreciação + Amortização ou EBITDA = Receita Total - Custos e Despesas Operacionais''')
              elif opcao_aprender == 7:
                  print('''
          A Participação de capital de terceiros é importante porque ajuda a avaliar o risco financeiro associado à dependência de recursos externos.
          Uma alta proporção de capital de terceiros pode indicar que a empresa está mais exposta a riscos financeiros, como flutuações nas taxas de juros e dificuldades para cumprir com suas obrigações.
          Além disso, comparar a Participação de capital de terceiros de diferentes empresas dentro do mesmo setor pode ajudar a identificar aquelas que possuem uma estrutura de capital mais equilibrada e menor risco financeiro.
          Participação de capital de terceiros = (Capital de Terceiros / Capital Total Investido) x 100''')
              elif opcao_aprender == 8:
                  print('''
          A Liquidez Corrente é importante porque indica a capacidade da empresa de cumprir suas obrigações de curto prazo, como pagamento de fornecedores, salários e dívidas de curto prazo.
          Uma Liquidez Corrente maior do que 1 sugere que a empresa possui ativos circulantes suficientes para cobrir seus passivos circulantes, o que pode ser um sinal de solidez financeira.
          No entanto, é importante notar que uma Liquidez Corrente muito alta pode indicar que a empresa não está utilizando seus recursos de forma eficiente e pode ter excesso de capital ocioso.
          Liquidez Corrente = Ativos Circulantes / Passivos Circulantes''')
              elif opcao_aprender == 9:
                  print('''
          A Liquidez Seca é importante porque fornece uma visão mais conservadora da capacidade da empresa de cumprir suas obrigações de curto prazo, excluindo a possibilidade de que seus estoques não possam ser convertidos em caixa rapidamente.
          Uma Liquidez Seca maior do que 1 sugere que a empresa possui ativos circulantes, excluindo estoques, suficientes para cobrir seus passivos circulantes, o que pode ser um sinal de solidez financeira.
          No entanto, assim como a Liquidez Corrente, é fundamental analisar a Liquidez Seca em conjunto com outros indicadores financeiros, como rentabilidade e endividamento, para obter uma visão mais abrangente da saúde financeira da empresa.
          Liquidez Seca = (Ativos Circulantes - Estoques) / Passivos Circulantes''')    
              elif opcao_aprender == 10:
                  print('''
          A Liquidez Imediata é importante porque fornece uma visão extremamente conservadora da capacidade da empresa de cumprir suas obrigações de curto prazo, considerando apenas o caixa e os equivalentes de caixa disponíveis.
          Um valor baixo de Liquidez Imediata pode indicar que a empresa não possui recursos suficientes para enfrentar situações de crise ou imprevistos financeiros.
          No entanto, a Liquidez Imediata não deve ser analisada isoladamente, já que ela não considera outros ativos circulantes que possam ser convertidos em caixa em um prazo relativamente curto.
          Liquidez Imediata = Caixa e Equivalentes de Caixa / Passivos Circulantes''')
              elif opcao_aprender == 11:
                  print("Voltando ao menu inicial.")
                  break
          else:
              print("Opção inválida.")
      
      elif opcao == 13:
        break