def relatorio(titulo, *notas, **infos):
	"""Imprime um relatório com título, notas, média e informações extras.

	titulo: str
	*notas: várias notas numéricas
	**infos: informações extras (professor, turma, etc.)
	"""
	print(f"Relatório: {titulo}")
	print(f"Notas: {notas}")
	if notas:
		media = sum(notas) / len(notas)
		print(f"Média: {media:.1f}")
	else:
		print("Média: N/A")

	if infos:
		print("Informações extras:")
		for chave, valor in infos.items():
			print(f"{chave}: {valor}")


if __name__ == '__main__':
	# Exemplo de uso
	relatorio('Matemática', 8, 7, 9, professor='Carlos', turma='2A')

