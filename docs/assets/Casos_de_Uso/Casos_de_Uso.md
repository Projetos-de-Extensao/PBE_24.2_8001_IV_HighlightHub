# Casos de Uso do HighlightHub
### Caso de Uso - Criar conta

**Pré-Condições:** 
- O usuário acessa o HighlightHub.

**Fluxo Principal:**

1. Usuário acessa a página home
2. Usuário clica no botão de sign in
3. Usuário preenche o formulário 
4. Usuário indica suas preferências em relação a esportes
5. Usuário é redirecionado a página home já logado

**Pós-Condições:**
- Conta é criada e suas informações são salvas com sucesso no banco de dados
- A página home filtra os posts para os gostos do usuário

---

### Caso de Uso - Salvar Playlists

**Pré-Condições:** 
- O usuário acessa o HighlightHub.

**Fluxo Principal:**

1. Usuário acessa a página home
2. Usuário clica no botão de sign in
3. Usuário preenche o formulário 
4. Usuário indica suas preferências em relação a esportes
5. Usuário é redirecionado a página home já logado

**Pós-Condições:**
- Conta é criada e suas informações são salvas com sucesso no banco de dados
- A página home filtra os posts para os gostos do usuário

---

# Casos de Uso - Highlights Hub

## Caso de Uso - Pesquisar Posts
**Pré-Condições:**
- O usuário está logado no HighlightHub.

**Fluxo Principal:**
1. O usuário acessa a barra de pesquisa na página principal.
2. O usuário digita um termo relacionado a um vídeo ou esporte de interesse.
3. O sistema sugere resultados conforme o termo digitado.
4. O usuário seleciona um dos resultados da pesquisa.
5. O sistema exibe o post ou vídeo correspondente.

**Pós-Condições:**
- O post ou vídeo correspondente é exibido ao usuário.
- O histórico de pesquisas pode ser salvo para melhorar sugestões futuras.

---

## Caso de Uso - Acessar Posts
**Pré-Condições:**
- O usuário está logado no HighlightHub.

**Fluxo Principal:**
1. O usuário acessa a página principal com posts destacados.
2. O usuário clica em um post de seu interesse.
3. O sistema carrega o conteúdo do post, exibindo o vídeo e informações associadas.

**Pós-Condições:**
- O post é exibido com todas as informações e o vídeo.

---

## Caso de Uso - Salvar Posts
**Pré-Condições:**
- O usuário está logado no HighlightHub.

**Fluxo Principal:**
1. O usuário navega até um post ou vídeo de interesse.
2. O usuário clica no botão "Salvar" no post.
3. O sistema armazena a ação e adiciona o post à lista de salvos do usuário.

**Pós-Condições:**
- O post é salvo na lista de favoritos do usuário.
- O sistema atualiza a página de salvos com o novo post.

---

## Caso de Uso - Curtir Posts
**Pré-Condições:**
- O usuário está logado no HighlightHub.

**Fluxo Principal:**
1. O usuário acessa um post de interesse.
2. O usuário clica no botão "Curtir".
3. O sistema registra a curtida no banco de dados e atualiza a contagem de curtidas.

**Pós-Condições:**
- A curtida do usuário é registrada no post.
- A contagem de curtidas é atualizada.

---

## Caso de Uso - Gerenciar Perfil de Usuário
**Pré-Condições:**
- O usuário está logado no HighlightHub.

**Fluxo Principal:**
1. O usuário acessa a página de perfil.
2. O usuário edita suas informações pessoais, como nome de usuário e preferências esportivas.
3. O sistema valida as informações e as atualiza no banco de dados.

**Pós-Condições:**
- As informações do perfil do usuário são atualizadas com sucesso.

---

## Caso de Uso - Receber Feed Personalizado
**Pré-Condições:**
- O usuário está logado e possui preferências cadastradas.

**Fluxo Principal:**
1. O sistema analisa as preferências do usuário salvas no perfil.
2. O sistema busca vídeos e posts relevantes com base nas preferências do usuário.
3. O feed personalizado é exibido na página inicial do usuário.

**Pós-Condições:**
- O usuário vê o feed com vídeos e posts que correspondem às suas preferências.

---

## Caso de Uso - Filtrar Posts
**Pré-Condições:**
- O usuário está logado no HighlightHub.

**Fluxo Principal:**
1. O usuário acessa a barra de filtro de posts.
2. O usuário seleciona critérios de filtro, como esporte, popularidade ou data de publicação.
3. O sistema aplica os filtros e exibe apenas os posts que correspondem aos critérios selecionados.

**Pós-Condições:**
- O feed de posts é filtrado de acordo com os critérios definidos pelo usuário.

---

## Caso de Uso - Adicionar Posts (Administrador)
**Pré-Condições:**
- O administrador está logado no sistema como administrador.

**Fluxo Principal:**
1. O administrador acessa o painel de administração.
2. O administrador clica na opção "Adicionar Post".
3. O sistema apresenta um formulário para o administrador preencher os detalhes do post, incluindo título, descrição e link do vídeo.
4. O administrador insere as informações e clica em "Salvar".
5. O sistema valida os dados e publica o post, tornando-o visível para os usuários.

**Pós-Condições:**
- O post é publicado e visível no feed de todos os usuários.
- As informações são salvas com sucesso no banco de dados.

---

## Caso de Uso - Remover Posts (Administrador)
**Pré-Condições:**
- O administrador está logado no sistema como administrador.

**Fluxo Principal:**
1. O administrador acessa o painel de administração.
2. O administrador seleciona a opção "Gerenciar Posts".
3. O sistema exibe uma lista de todos os posts disponíveis.
4. O administrador localiza o post que deseja remover e clica em "Remover".
5. O sistema pede confirmação para a remoção.
6. O administrador confirma a ação.
7. O sistema remove o post do banco de dados e do feed dos usuários.

**Pós-Condições:**
- O post é removido com sucesso e não é mais visível para os usuários.
- A remoção é registrada no sistema para auditoria, se necessário.

---

## Caso de Uso - Acessar Site como Internauta Visitante
**Pré-Condições:**
- O internauta visitante acessa o site "Highlights Hub" sem ter uma conta e sem realizar login.

**Fluxo Principal:**
1. O internauta visita a página inicial do "Highlights Hub".
2. O sistema carrega e exibe um feed padrão de vídeos e posts.
3. O internauta navega pelos posts disponíveis no site.
4. O internauta pode visualizar os vídeos e as informações associadas aos posts.
5. Caso o internauta tente curtir, salvar ou comentar, o sistema exibe uma mensagem solicitando que ele faça login ou crie uma conta.

**Pós-Condições:**
- O internauta pode visualizar os vídeos e posts públicos do site, mas não tem acesso a funcionalidades interativas (como curtir ou salvar).
- A experiência é limitada à visualização de conteúdo, sem personalizações ou modificações no perfil.
