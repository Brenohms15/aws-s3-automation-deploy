# AWS Cloud Hosting & Automation Project 🚀

Este projeto demonstra a implementação de uma arquitetura de hospedagem estática utilizando serviços da **Amazon Web Services (AWS)** e automação via Python.

## 🛠️ Arquitetura
- **Amazon S3**: Hospedagem dos arquivos estáticos com configuração de Bucket Website.
- **Boto3 (Python SDK)**: Script automatizado para deploy e sincronização de arquivos locais com a nuvem.
- **IAM**: Configuração de políticas de acesso seguindo o princípio de menor privilégio.

## 🚀 Como funciona
O projeto consiste em um site estático cujos arquivos são gerenciados localmente e enviados para a infraestrutura AWS através de um script de automação, eliminando a necessidade de upload manual via console.

### Pré-requisitos
- Conta AWS com permissões de S3.
- AWS CLI configurado localmente.
- Python 3.x e biblioteca `boto3`.

## 🔒 Segurança
As credenciais de acesso (Access Keys) não estão expostas neste repositório, sendo gerenciadas via variáveis de ambiente e protegidas pelo `.gitignore`, seguindo as melhores práticas de segurança da AWS.