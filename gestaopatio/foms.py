from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, DateTimeField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed


class FormCriarConta(FlaskForm):
        hierarquia = [
            ('Admin','Admin'), ('Operator','Operator'),
            ('User','User'), ('Customer','Customer')]
        username = StringField('Nome Usuário', validators=[DataRequired()])
        email = StringField('E-mail Usuário', validators=[DataRequired(), Email()])
        senha = PasswordField('Senha Usuário', validators=[DataRequired(), Length(9, 15)])
        hierarquia_user = SelectField('Hierarquia do Usuário', choices=hierarquia, validators=[DataRequired()])
        botao_submit_criar = SubmitField('Enviar')
    
def validate_email(self, email):
        email_user = Usuario.query.filter_by(email=email.data).first()
        if email_user:
            raise ValidationError('E-mail já cadastrado! Cadastre outro e-mail ou faça logín com seu usuário!')
            
    
class FormLogin(FlaskForm):
        username = StringField('E-mail Usuário', validators=[DataRequired(), Email()])
        senha = PasswordField('Senha Usuário', validators=[DataRequired(), Length(9, 15)])
        lembrar_dados = BooleanField('Lembrar Acesso')
        botao_submit_login = SubmitField('Login')
    
    
class FormAgendamentos(FlaskForm):
        intervalos = [
            ('00:00', '00:00'), ('00:30', '00:30'), ('01:00', '01:00'), ('01:30', '01:30'),
            ('02:00', '02:00'), ('02:30', '02:30'), ('03:00', '03:00'), ('03:30', '03:30'),
            ('04:00', '04:00'), ('04:30', '04:30'), ('05:00', '05:00'), ('05:30', '05:30'),
            ('06:00', '06:00'), ('06:30', '06:30'), ('07:00', '07:00'), ('07:30', '07:30'),
            ('08:00', '08:00'), ('08:30', '08:30'), ('09:00', '09:00'), ('09:30', '09:30'),
            ('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'),
            ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('13:30', '13:30'),
            ('14:00', '14:00'), ('14:30', '14:30'), ('21:00', '21:00'), ('21:30', '21:30'),
            ('22:00', '22:00'), ('22:30', '22:30'), ('23:00', '23:00'), ('23:30', '23:30')]
        City = [(''), ('ARACAJU'), ('ARARAQUARA'), ('ARAUCARIA'), ('BANGU'), ('BELEM'), ('BELO HORIZONTE'), ('BETIM')
                          , ('BOA VISTA'), ('BRASILIA'), ('CD ANHANGUERA'), ('CABO DE SANTO AGOSTINHO'), ('CAJAMAR'), ('CAJU'), ('CAMPO GRANDE'), ('CAMPOS'), ('CAMPOS DOS GOYTACAZES')
                          , ('CARIACICA'), ('CURITIBA'), ('DUQUE DE CAXIAS'), ('FARROUPILHA'), ('FRANCA'), ('ITU'), ('JACAREPAGUA'), ('JOAO PESSOA'), ('JUNDIAI'), ('MACAIBA')
                          , ('MACEIO'), ('MANAUS'), ('MARACANAU'), ('MARILIA'), ('MARINGA'), ('MOCOCA'), ('MOGI DAS CRUZES'), ('NOVA IGUAÇU'), ('OSASCO'), ('PASSOS')
                          , ('PORTO ALEGRE'), ('PORTO REAL'), ('PORTO VELHO'), ('RIBEIRAO PRETO'), ('SANTA MARIA'), ('SANTO ANDRE'), ('SAO JOAO DA BOA VISTA'), ('SAO LUIS'), ('SAO PAULO')
                          , ('SAO PEDRO DA ALDEIA'), ('SIMOES FILHO'), ('SOROCABA'), ('SUMARE'), ('TERESINHA'), ('TRINDADE'), ('UBERLANDIA'), ('VARZEA GRANDE'), ('VITORIA DA CONQUISTA')]
        Tfrota = [(''), ('RODOTREM'), ('CARRETA'),
                  ('BI-TRUCK'),('TRUCK'),
                  ('TOCO'), ('VULC')]
        TOperacao = [(''), ('Recebimento'), ('Expedição')]
    
        entrydate = DateField('Data Agenda', format='%Y-%m-%d', validators=[DataRequired()] )
        entryhour = SelectField('Hora Agenda', choices=intervalos, validators=[DataRequired()] )
        origem = SelectField('Origem', choices=City, validators=[DataRequired()] )
        destino = SelectField('Destino', choices=City, validators=[DataRequired()] )
        veiculo = SelectField('Tipo de Veículo', choices=Tfrota, validators=[DataRequired()] )
        cliente = StringField('Cliente', validators=[DataRequired()])
        placa_veiculo = StringField('Placa', validators=[DataRequired(), Length(7)])
        motorista = StringField('Motorita', validators=[DataRequired()])
        transportadora = StringField('Transportadora', validators=[DataRequired()])
        tipo_operacao = SelectField('Operação', choices=TOperacao, validators=[DataRequired()] )
        botao_submit_agendamento = SubmitField('Agendar')
        
    
    
class FormReagenda(FlaskForm):
        intervalos = [
            ('00:00', '00:00'), ('00:30', '00:30'), ('01:00', '01:00'), ('01:30', '01:30'),
            ('02:00', '02:00'), ('02:30', '02:30'), ('03:00', '03:00'), ('03:30', '03:30'),
            ('04:00', '04:00'), ('04:30', '04:30'), ('05:00', '05:00'), ('05:30', '05:30'),
            ('06:00', '06:00'), ('06:30', '06:30'), ('07:00', '07:00'), ('07:30', '07:30'),
            ('08:00', '08:00'), ('08:30', '08:30'), ('09:00', '09:00'), ('09:30', '09:30'),
            ('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'),
            ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('13:30', '13:30'),
            ('14:00', '14:00'), ('14:30', '14:30'), ('21:00', '21:00'), ('21:30', '21:30'),
            ('22:00', '22:00'), ('22:30', '22:30'), ('23:00', '23:00'), ('23:30', '23:30')]
        motivos = [(' ',' '),('ALTERAÇÃO MOTORISTA/PLACA','ALTERAÇÃO MOTORISTA/PLACA'),('NO SHOW','NO SHOW'), ('CAPACIDADE LOGISTICA','CAPACIDADE LOGISTICA'),
                  ('CANCELAMENTO COLETA CLIENTE','CANCELAMENTO COLETA CLIENTE'), 
                   ('CANCELAMENTO CARGA LOGÍSTICA', 'CANCELAMENTO CARGA LOGÍSTICA')]
        TOperacao = [(''), ('Recebimento'), ('Expedição')]
        Tfrota = [(''), ('RODOTREM'),('CARRETA'),
                  ('BI-TRUCK'),('TRUCK'),
                  ('TOCO'), ('VULC')]
        num_transporte = StringField('Transporte', validators=[DataRequired()] )
        entrydate = DateField('Data Agenda', format='%Y-%m-%d', validators=[DataRequired()] )
        entryhour = SelectField('Hora Agenda', choices=intervalos, validators=[DataRequired()] )
        origem = StringField('Origem', validators=[DataRequired()] )
        destino = StringField('Destino', validators=[DataRequired()] )
        veiculo = SelectField('Tipo Veículo', choices=Tfrota, validators=[DataRequired()] )
        cliente = StringField('Cliente', validators=[DataRequired()])
        placa_veiculo = StringField('Placa', validators=[DataRequired(), Length(7)])
        motorista = StringField('Motorita', validators=[DataRequired()])
        transportadora = StringField('Transportadora', validators=[DataRequired()])
        tipo_operacao = SelectField('Operação', choices=TOperacao, validators=[DataRequired()] )
        motivo_reagenda = SelectField('Motivo', choices=motivos, validators=[DataRequired()] )
        botao_submit_reagendar = SubmitField('Reagendar')
        botao_submit_alterar = SubmitField('Alterar')
        botao_submit_cancelar = SubmitField('Cancelar')
       
    
class FormFrota(FlaskForm):
        Tfrota = [(''), ('RODOTREM'),('CARRETA'),
                  ('BI-TRUCK'),('TRUCK'),
                  ('TOCO'), ('VULC')]
        Tstatus = [('ATIVO'),('ATIVO'), ('INATIVO'),('INATIVO')]
        num_frota = StringField('Frota', validators=[DataRequired()] )
        placa_frota = StringField('Placa', validators=[DataRequired()] )
        capacidade_frota = IntegerField('Capacidade', validators=[DataRequired()] )
        tipo_frota = SelectField('Tipo Frota', choices=Tfrota, validators=[DataRequired()] )
        status_frota = SelectField('Tipo Frota', choices=Tstatus, validators=[DataRequired()] )
    
class FormCliente(FlaskForm):
        UF_cliente = [(''), ('AC'), ('AL'), ('AM'), ('AP'), ('BA'), ('CE'), ('DF'), ('ES'), ('GO') , ('MA'), ('MG'), ('MS'), ('MT'), ('PA')
                     , ('PB'), ('PE'), ('PI'), ('PR'), ('RJ'), ('RN'), ('RO'), ('RR'), ('RS'), ('SC'), ('SE'), ('SP'), ('TO') ]
        City_cliente = [(''), ('ARACAJU'), ('ARARAQUARA'), ('ARAUCARIA'), ('BANGU'), ('BELEM'), ('BELO HORIZONTE'), ('BETIM')
                          , ('BOA VISTA'), ('BRASILIA'), ('CD ANHANGUERA'), ('CABO DE SANTO AGOSTINHO'), ('CAJAMAR'), ('CAJU'), ('CAMPO GRANDE'), ('CAMPOS'), ('CAMPOS DOS GOYTACAZES')
                          , ('CARIACICA'), ('CURITIBA'), ('DUQUE DE CAXIAS'), ('FARROUPILHA'), ('FRANCA'), ('ITU'), ('JACAREPAGUA'), ('JOAO PESSOA'), ('JUNDIAI'), ('MACAIBA')
                          , ('MACEIO'), ('MANAUS'), ('MARACANAU'), ('MARILIA'), ('MARINGA'), ('MOCOCA'), ('MOGI DAS CRUZES'), ('NOVA IGUAÇU'), ('OSASCO'), ('PASSOS')
                          , ('PORTO ALEGRE'), ('PORTO REAL'), ('PORTO VELHO'), ('RIBEIRAO PRETO'), ('SANTA MARIA'), ('SANTO ANDRE'), ('SAO JOAO DA BOA VISTA'), ('SAO LUIS'), ('SAO PAULO')
                          , ('SAO PEDRO DA ALDEIA'), ('SIMOES FILHO'), ('SOROCABA'), ('SUMARE'), ('TERESINHA'), ('TRINDADE'), ('UBERLANDIA'), ('VARZEA GRANDE'), ('VITORIA DA CONQUISTA')]
        OP_cliente = [(''), ('MERCADO EXTERNO'), ('MERCADOR INTERNO'),
                     ('TRANSFERÊNCIA')]
        nome_cliente = StringField('Nome Cliente', validators=[DataRequired()] )
        cnpj_cliente = StringField('CNPJ Cliente', validators=[DataRequired()] )
        cidade_cliente = SelectField('Cidade', choices=City_cliente, validators=[DataRequired()] )
        estado_cliente = SelectField('Estado', choices=UF_cliente, validators=[DataRequired()] )
        operacao_cliente = SelectField('Operação', choices=OP_cliente, validators=[DataRequired()] )
        botao_submit_cliente = SubmitField('Salvar Cliente')
    
class FormEmbarcador(FlaskForm):
        UF_embarcador = [(''), ('AC'), ('AL'), ('AM'), ('AP'), ('BA'), ('CE'), ('DF'), ('ES'), ('GO') , ('MA'), ('MG'), ('MS'), ('MT'), ('PA')
                     , ('PB'), ('PE'), ('PI'), ('PR'), ('RJ'), ('RN'), ('RO'), ('RR'), ('RS'), ('SC'), ('SE'), ('SP'), ('TO') ]
        City_embarcador = [(''), ('ARACAJU'), ('ARARAQUARA'), ('ARAUCARIA'), ('BANGU'), ('BELEM'), ('BELO HORIZONTE'), ('BETIM')
                          , ('BOA VISTA'), ('BRASILIA'), ('CD ANHANGUERA'), ('CABO DE SANTO AGOSTINHO'), ('CAJAMAR'), ('CAJU'), ('CAMPO GRANDE'), ('CAMPOS'), ('CAMPOS DOS GOYTACAZES')
                          , ('CARIACICA'), ('CURITIBA'), ('DUQUE DE CAXIAS'), ('FARROUPILHA'), ('FRANCA'), ('ITU'), ('JACAREPAGUA'), ('JOAO PESSOA'), ('JUNDIAI'), ('MACAIBA')
                          , ('MACEIO'), ('MANAUS'), ('MARACANAU'), ('MARILIA'), ('MARINGA'), ('MOCOCA'), ('MOGI DAS CRUZES'), ('NOVA IGUAÇU'), ('OSASCO'), ('PASSOS')
                          , ('PORTO ALEGRE'), ('PORTO REAL'), ('PORTO VELHO'), ('RIBEIRAO PRETO'), ('SANTA MARIA'), ('SANTO ANDRE'), ('SAO JOAO DA BOA VISTA'), ('SAO LUIS'), ('SAO PAULO')
                          , ('SAO PEDRO DA ALDEIA'), ('SIMOES FILHO'), ('SOROCABA'), ('SUMARE'), ('TERESINHA'), ('TRINDADE'), ('UBERLANDIA'), ('VARZEA GRANDE'), ('VITORIA DA CONQUISTA')]
        nome_embarcador = StringField('Nome Embarcador', validators=[DataRequired()] )
        cnpj_embarcador = StringField('CNPJ Embarcador', validators=[DataRequired()] )
        cidade_embarcador = SelectField('Cidade Embarcador', choices=City_embarcador, validators=[DataRequired()] )
        estado_embarcador = SelectField('Estado Embarcador', choices=UF_embarcador, validators=[DataRequired()] )
        botao_submit_embarcador = SubmitField('Salvar Embarcador')
    
class FormFrotaTerceiro(FlaskForm):
        TCarro = [(''), ('RODOTREM'), ('CARRETA'),
                  ('BI-TRUCK'),('TRUCK'),
                  ('TOCO'), ('VULC')]
        nome_transportador = StringField('Transportadora', validators=[DataRequired()] )
        cnpj_transportador = StringField('CNPJ Transportadora', validators=[DataRequired()] )
        email_transportador = StringField('E-mail Transportador', validators=[DataRequired(), Email()])
        tipo_frota_transportador = SelectField('Tipo Veículo Transportador', choices=TCarro, validators=[DataRequired()] )
        placa_carreta = StringField('Placa Carreta', validators=[DataRequired()] )
    
class FormMotorista(FlaskForm):
        nome_motorista = StringField('Nome Motorista', validators=[DataRequired()] )
        celular = StringField('Phone', validators=[DataRequired()])
        transportadora = StringField('Transportadora', validators=[DataRequired()] )
        CPF_motorista = StringField('CPF Motorista', validators=[DataRequired()] )
        habilitação = StringField('Habilitação', validators=[DataRequired()] )
        validade_habilitacao = StringField('Validade Habilitação', validators=[DataRequired()] )
        foto_motorista = FileField('Foto Motorista', validators=[FileAllowed('jpg', 'png')] )
        botao_submit_motorista = SubmitField('Cadastrar')

class FormControlPatio(FlaskForm):
        num_frota = StringField('Frota', validators=[DataRequired()] )
        num_transporte = StringField('Transporte', validators=[DataRequired()] )
        num_doca = StringField('Stage-In')
        num_faixa = StringField('Faixa')
        num_posicao = StringField('Posição')
        sub_frota = StringField('Frota Substituta')
        botao_submit_controlpatio = SubmitField('Cadastrar')

class FormControlFaixa(FlaskForm):
        num_frota = StringField('Frota', validators=[DataRequired()] )
        num_transporte = StringField('Transporte', validators=[DataRequired()] )
        num_doca = StringField('Stage-In')
        num_faixa = StringField('Faixa')
        num_posicao = StringField('Posição')
        sub_frota = StringField('Frota Substituta')
        botao_submit_controlpatio = SubmitField('Cadastrar')
