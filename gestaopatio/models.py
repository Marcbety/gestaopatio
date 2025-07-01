from gestaopatio import database
from datetime import date, datetime, time, timezone, timedelta

  
class Usuario(database.Model, UserMixin):
        id = database.Column(database.Integer, primary_key=True)
        username = database.Column(database.String, nullable=False)
        email = database.Column(database.String, nullable=False, unique=True)
        senha = database.Column(database.String, nullable=False)
        hierarquia = database.Column(database.String, nullable=False, default='Customer')
        foto_perfil = database.Column(database.String, default='default.jpg')
        data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
        ultima_alteracao = database.Column(database.DateTime, nullable=False)
        usuario_alteracao = database.Column(database.String, nullable=False)
    
    
class Agendamentos(database.Model):
        id = database.Column(database.Integer, primary_key=True)
        num_transporte = database.Column(database.String)
        entrydate = database.Column(database.Date, nullable=False)
        entryhour = database.Column(database.String, nullable=False)
        origem = database.Column(database.String, nullable=False)
        destino = database.Column(database.String, nullable=False)
        veiculo = database.Column(database.String, nullable=False)
        cliente = database.Column(database.String, nullable=False)
        placa_veiculo = database.Column(database.String, nullable=False)
        motorista = database.Column(database.String, nullable=False)
        transportadora = database.Column(database.String, nullable=False)
        tipo_operacao = database.Column(database.String)
        check_in = database.Column(database.DateTime)
        entrada_patio = database.Column(database.DateTime)
        carregamento = database.Column(database.DateTime)
        fim_carregamento = database.Column(database.DateTime)
        saida_portaria = database.Column(database.DateTime)
        fase_carga = database.Column(database.String)
        status_carga = database.Column(database.String)
        motivo_reagenda = database.Column(database.String)
        NF_recebida = database.Column(database.LargeBinary)
        data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
        ultima_alteracao = database.Column(database.DateTime, nullable=False)
        usuario_alteracao = database.Column(database.String, nullable=False)
    
    
class Motorista(database.Model):
        id = database.Column(database.Integer, primary_key=True)
        nome_motorista = database.Column(database.String, nullable=False)
        celular = database.Column(database.String, nullable=False, unique=True)
        transportadora = database.Column(database.String, nullable=False)
        CPF_motorista = database.Column(database.String, nullable=False, unique=True)
        habilitação = database.Column(database.String, nullable=False, unique=True)
        validade_habilitacao = database.Column(database.Date, nullable=False)
        foto_motorista = database.Column(database.String, default='default.jpg')
        data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
        ultima_alteracao = database.Column(database.DateTime, nullable=False)
        usuario_alteracao = database.Column(database.String, nullable=False)
    
    
    
class Frota_Andina(database.Model): 
        id = database.Column(database.Integer, primary_key=True)
        num_frota = database.Column(database.String, nullable=False)
        placa_frota = database.Column(database.String, nullable=False)
        capacidade_frota = database.Column(database.Integer, nullable=False)
        tipo_frota = database.Column(database.String, nullable=False)
        status_frota = database.Column(database.String, nullable=False)
        data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
        ultima_alteracao = database.Column(database.DateTime, nullable=False)
        usuario_alteracao = database.Column(database.String, nullable=False)
    
    
class Cliente_Andina(database.Model):
        id = database.Column(database.Integer, primary_key=True)
        nome_cliente = database.Column(database.String, nullable=False)
        cnpj_cliente = database.Column(database.String, nullable=False, unique=True)
        cidade_cliente = database.Column(database.String, nullable=False)
        estado_cliente = database.Column(database.String, nullable=False)
        operacao_cliente = database.Column(database.String, nullable=False)
        data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
        #ultima_alteracao = database.Column(database.DateTime, nullable=False)
        #usuario_alteracao = database.Column(database.String, nullable=False)
    
class Embarcador_Andina(database.Model):
        id = database.Column(database.Integer, primary_key=True)
        nome_embarcador = database.Column(database.String, nullable=False)
        cnpj_embarcador = database.Column(database.String, nullable=False, unique=True)
        cidade_embarcador = database.Column(database.String, nullable=False)
        estado_embarcador = database.Column(database.String, nullable=False)
        data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
        ultima_alteracao = database.Column(database.DateTime, nullable=False)
        usuario_alteracao = database.Column(database.String, nullable=False)
    
    
class Frota_Terceiros(database.Model):
        id = database.Column(database.Integer, primary_key=True)
        nome_transportador = database.Column(database.String, nullable=False)
        cnpj_transportador = database.Column(database.String, nullable=False)
        email_transportador = database.Column(database.String, nullable=False)
        tipo_frota_transportador = database.Column(database.String, nullable=False)
        placa_carreta = database.Column(database.String, nullable=False)
        data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
        ultima_alteracao = database.Column(database.DateTime, nullable=False)
        usuario_alteracao = database.Column(database.String, nullable=False)



class Arquivos(database.Model):
        id = database.Column(database.Integer, primary_key=True)
        arquivo = database.Column(database.String, nullable=False)
        data_arquivo = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
        ultima_alteracao = database.Column(database.DateTime, nullable=False)
        usuario_alteracao = database.Column(database.String, nullable=False)
        
class Vendas_ME(database.Model):
        id = database.Column(database.Integer, primary_key=True)
        data = database.Column(database.Date, nullable=False)
        cod_cliente = database.Column(database.String, nullable = False)
        cliente = database.Column(database.String, nullable = False)
        destino = database.Column(database.String, nullable = False)
        num_transporte = database.Column(database.String, nullable = False)
        cod_produto = database.Column(database.String, nullable = False)
        descricao = database.Column(database.String, nullable = False)
        qtd_cxf = database.Column(database.String, nullable = False)
        qtd_unitaria = database.Column(database.String, nullable = False)
        transportadora = database.Column(database.String, nullable = False)
        placa_veiculo = database.Column(database.String, nullable = False)
        centro = database.Column(database.String, nullable = False)
        buscar = database.Column(database.String, nullable = False)
        somatoria_buscar = database.Column(database.String, nullable = False)
        ad_transporte = database.Column(database.String, nullable = False)
        transporte_adicionar = database.Column(database.String, nullable = False)
        motorista = database.Column(database.String, nullable = False)
        data_producao= database.Column(database.Date)
        guia_gnre = database.Column(database.Boolean, default=False)
        ultima_alteracao = database.Column(database.DateTime, nullable=False)
        usuario_alteracao = database.Column(database.String, nullable=False)

class Control_Patio(database.Model):
        id = database.Column(database.Integer, primary_key=True)
        data = database.Column(database.Date, nullable=False)
        num_transporte = database.Column(database.String, nullable = False)
        num_frota = database.Column(database.String, nullable = False)
        num_doca = database.Column(database.String)
        num_faixa = database.Column(database.String)
        num_posicao = database.Column(database.String)
        sub_frota = database.Column(database.String)
        hora_portaria = database.Column(database.DateTime)
        hora_patio = database.Column(database.DateTime)
        hora_faixa = database.Column(database.DateTime)
        hora_conclusao = database.Column(database.DateTime)
        status_frota = database.Column(database.String)
        status_faixa = database.Column(database.String)
        ultima_alteracao = database.Column(database.DateTime, nullable=False)
        usuario_alteracao = database.Column(database.String, nullable=False)
        
    
        @property
        def tempo_faixa(self):
            if self.hora_faixa:
                hora_faixa_local = self.hora_faixa.replace(tzinfo=None)
                if self.hora_conclusao:
                    hora_conclusao_local = self.hora_conclusao.replace(tzinfo=None)
                    return hora_conclusao_local - hora_faixa_local
                else:
                    return datetime.now() - hora_faixa_local
            return None

class ControlPicking(database.Model):
         id = database.Column(database.Integer, primary_key=True)
         data_doc = database.Column(database.DateTime, nullable=False)
         hora_conf_piso = database.Column(database.DateTime)
         hora_checkout = database.Column(database.DateTime)
         data_remessa = database.Column(database.DateTime)
         num_palete = database.Column(database.String, nullable = False)
         conf_checkout = database.Column(database.String)
         conf_piso = database.Column(database.String)
         tipo_remessa = database.Column(database.String, nullable = False)
         num_transporte = database.Column(database.String, nullable = False)
         num_remessa = database.Column(database.String, nullable = False)
         material = database.Column(database.String, nullable = False)
         descricao = database.Column(database.String, nullable = False)
         qtd_remessa = database.Column(database.String, nullable = False)
         num_UD = database.Column(database.String, nullable = False)
         status_material = database.Column(database.String, nullable = False)
         num_posicao = database.Column(database.String, nullable = False)
         pickeador = database.Column(database.String)
         tipo_palete = database.Column(database.String)
         hora_confirmacao = database.Column(database.DateTime)
         ultima_alteracao = database.Column(database.DateTime, nullable=False)
         usuario_alteracao = database.Column(database.String, nullable=False)

class Pente_fino(database.Model):
        id = database.Column(database.Integer, primary_key=True)
        data_pf = database.Column(database.DateTime, nullable=False)
        num_frota = database.Column(database.String, nullable=False)
        num_UD = database.Column(database.String, nullable = False)
        tipo_erro = database.Column(database.String, nullable = False)
        produto = database.Column(database.String, nullable = False)
        qtd = database.Column(database.Integer, nullable = False)
        prod_trocado = database.Column(database.String)
        qtd_trocado = database.Column(database.Integer)
        auditor = database.Column(database.String, nullable = False)
