# Documentación para CloudFormation Stack
Esta configuración corresponde a un stack de CloudFormation para implementar una infraestructura que contiene:
- Un *Auto Scalling Group* (ASG), el cual implementa dos instancias de EC2
- *Load Balancer*
- *Security Group*
## Requisitos
Dentro de una misma región, haber creado un ´KeyPair´ para ser entregado como parámetro, Un `VPC` y los `Subnets`dentro de este.
## Parámetros
Los parámetros necesarios para realizar el proceso de construcción (crear el stack) son:
- `KeyName`: entrega_final_keypair
- `VpcId`: vpc-b97e6bde
- `Subnets`: subnet-aabd79cc, subnet-aabd79cc
- `InstanceType`(*default*): t2.micro
- `SSHLocation`(*default*): 0.0.0.0/0
  
