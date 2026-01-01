# Arena Manager Web

Sistema completo de gerenciamento de reservas de quadras esportivas com autenticação de usuários e painel administrativo.

##  Recursos

### Para Usuários
-  Visualizar e agendar reservas de quadras
-  Filtrar quadras por data e horário disponível
-  Gerenciar perfil pessoal
-  Consultar histórico de reservas
-  Cancelar reservas quando necessário

### Para Administradores
-  Painel de controle completo
-  Gerenciar quadras (CRUD)
-  Gerenciar usuários
-  Gerenciar agendas e horários
-  Visualizar todas as reservas

##  Tecnologias Utilizadas

- **Frontend**: React 18 + TypeScript
- **Build Tool**: Vite
- **Styling**: Tailwind CSS
- **UI Components**: shadcn/ui
- **Notificações**: Sonner
- **Forms**: React Hook Form + Zod
- **Routing**: React Router v6
- **HTTP Client**: Fetch API
- **Deployment**: Vercel

##  Instalação

### Pré-requisitos
- Node.js 18+
- npm ou yarn

### Passos

1. **Clone o repositório**
``bash
git clone https://github.com/antonioclaudioofc/arena_manager.git
cd arena_manager
``

2. **Instale as dependências**
``bash
npm install
``

3. **Inicie o servidor de desenvolvimento**
``bash
npm run dev
``


##  Scripts Disponíveis

``bash
# Desenvolvimento
npm run dev          # Inicia servidor de desenvolvimento com HMR

# Build
npm run build        # Compila para produção

# Pré-visualização
npm run preview      # Pré-visualiza build de produção localmente

# Linting
npm run lint         # Verifica erros de código com ESLint
``

##  Autenticação

### Demo Rápido
Você pode testar o aplicativo com credenciais de demo na página de login:

- **Admin**
- **User**

### Fluxo de Autenticação
1. Login com credenciais
2. Token JWT armazenado localmente
3. Redirecionamento automático baseado em role (admin/user)
4. Token incluído em todas as requisições autenticadas

##  Estrutura do Projeto

``
src/
 assets/           # Imagens e ícones
 components/       # Componentes reutilizáveis
    Button.tsx
    CourtList.tsx
    Form.tsx
    Input.tsx
    Label.tsx
    ScheduleCard.tsx
    Sonner.tsx
 context/          # Context API para estado global
    AuthContext.tsx
 lib/              # Utilitários
    utils.ts
 pages/            # Páginas da aplicação
    Home.tsx
    Login.tsx
    Register.tsx
    Profile.tsx
    UserReservations.tsx
    Dashboard.tsx
    AdminCourts.tsx
    AdminUsers.tsx
    AdminReservations.tsx
    AdminSchedules.tsx
 routes/           # Proteção de rotas
    ProtectedRoute.tsx
    PublicRoute.tsx
 App.tsx           # Componente raiz
 main.tsx          # Entrada da aplicação
 index.css         # Estilos globais
``

##  API Backend

A aplicação conecta-se a um backend FastAPI:
``
Base URL: https://arena-manager-bvlw.onrender.com
``

### Endpoints principais:
- POST /auth/token - Autenticação
- GET / - Listar quadras
- GET /schedule/ - Listar horários
- GET /reservation/ - Listar reservas do usuário
- POST /reservation/ - Criar reserva
- DELETE /reservation/{id} - Cancelar reserva
- GET /admin/* - Endpoints administrativos

##  Funcionalidades em Detalhes

### Página Home
- Header com branding e controles de usuário
- Data pills para selecionar dia
- Lista de quadras com horários disponíveis
- Botão de agendamento direto
- Para admins: botão de acesso ao dashboard

### Área do Usuário
- **Perfil**: Visualizar informações pessoais
- **Minhas Reservas**: Listar e cancelar reservas

### Painel Admin
- **Quadras**: Adicionar, editar, deletar
- **Usuários**: Listar e remover usuários
- **Horários**: Gerenciar agenda de disponibilidade
- **Reservas**: Visualizar todas as reservas do sistema

##  Desenvolvedor

**Antônio Claudio**
- GitHub: [@antonioclaudioofc](https://github.com/antonioclaudioofc)