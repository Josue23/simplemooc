from django.db import models


class Course(models.Model):

	# name - é ao nivel de programaçao
	# Nome - é ao nivel do usuário
	name = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Atalho')  # SlugField é um CharField alterado

	# TextField é um campo CharField que não tem tamaho máximo
	description = models.TextField('Descrição', blank=True)

	# DateField - data
	start_date = models.DateField(
		'Data de início', null=True, blank=True  # blank=True - o campo não é obrigatório
		)  # null=True - pode ser nullable a nivel de banco de dados, pode retornar None

	image = models.ImageField(
		# upload_to - é o diretorio relativo a MEDIA_ROOT que está configurado no settings.py
		upload_to='courses/images',
		verbose_name='Imagem',
		null=True,
		blank=True
		)

	# models.DateTimeField - data e hora
	# auto_now_add=True - va salvar a data e hora apenas uma vez, no momento que criar o curso
	created_at =models.DateTimeField(
		'Criado em',
		auto_now_add=True
		)

	# models.DateTimeField - data e hora
	# auto_now=True - toda vez qu forsalvo vai alterar a variavel updated_at para a data e hora atual
	updated_at =models.DateTimeField(
		'Atualizado em',
		auto_now=True
		)