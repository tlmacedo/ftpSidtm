# Tracking file by folder pattern:  migrations
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Fiscalcestncm(models.Model):
    segmento = models.CharField(max_length=100)
    descricao = models.CharField(max_length=600)
    cest = models.CharField(max_length=7)
    ncm = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'fiscalCestNcm'


class Fiscalcstorigem(models.Model):
    id = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=180)

    class Meta:
        managed = False
        db_table = 'fiscalCstOrigem'


class Fiscalfretesituacaotributaria(models.Model):
    id = models.CharField(primary_key=True, max_length=2)
    descricao = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'fiscalFreteSituacaoTributaria'


class Fiscalfretetomadorservico(models.Model):
    id = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'fiscalFreteTomadorServico'


class Fiscalicms(models.Model):
    id = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'fiscalIcms'


class Fiscalmodelonfecte(models.Model):
    id = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'fiscalModeloNfeCte'


class Fiscalpiscofins(models.Model):
    descricao = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'fiscalPisCofins'


class Fiscaltributosefazam(models.Model):
    id = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'fiscalTributoSefazAm'


class RelcontatoEmailhomepage(models.Model):
    tabcontato = models.ForeignKey('Tabcontato', models.DO_NOTHING,
                                   db_column='tabContato_id')  # Field name made lowercase.
    tabemailhomepage = models.ForeignKey('Tabemailhomepage', models.DO_NOTHING,
                                         db_column='tabEmailHomePage_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relContato_EmailHomePage'


class RelcontatoTelefone(models.Model):
    tabcontato = models.ForeignKey('Tabcontato', models.DO_NOTHING,
                                   db_column='tabContato_id')  # Field name made lowercase.
    tabtelefone = models.ForeignKey('Tabtelefone', models.DO_NOTHING,
                                    db_column='tabTelefone_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relContato_Telefone'


class RelempresaContato(models.Model):
    tabempresa = models.ForeignKey('Tabempresa', models.DO_NOTHING,
                                   db_column='tabEmpresa_id')  # Field name made lowercase.
    tabcontato = models.ForeignKey('Tabcontato', models.DO_NOTHING,
                                   db_column='tabContato_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relEmpresa_Contato'


class RelempresaEmailhomepage(models.Model):
    tabempresa = models.ForeignKey('Tabempresa', models.DO_NOTHING,
                                   db_column='tabEmpresa_id')  # Field name made lowercase.
    tabemailhomepage = models.ForeignKey('Tabemailhomepage', models.DO_NOTHING,
                                         db_column='tabEmailHomePage_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relEmpresa_EmailHomePage'


class RelempresaEndereco(models.Model):
    tabempresa = models.ForeignKey('Tabempresa', models.DO_NOTHING,
                                   db_column='tabEmpresa_id')  # Field name made lowercase.
    tabendereco = models.ForeignKey('Tabendereco', models.DO_NOTHING,
                                    db_column='tabEndereco_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relEmpresa_Endereco'


class RelempresaInformacaorf(models.Model):
    tabempresa = models.ForeignKey('Tabempresa', models.DO_NOTHING,
                                   db_column='tabEmpresa_id')  # Field name made lowercase.
    tabinformacaoreceitafederal = models.ForeignKey('Tabinformacaoreceitafederal', models.DO_NOTHING,
                                                    db_column='tabInformacaoReceitaFederal_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relEmpresa_InformacaoRF'


class RelempresaTelefone(models.Model):
    tabempresa = models.ForeignKey('Tabempresa', models.DO_NOTHING,
                                   db_column='tabEmpresa_id')  # Field name made lowercase.
    tabtelefone = models.ForeignKey('Tabtelefone', models.DO_NOTHING,
                                    db_column='tabTelefone_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relEmpresa_Telefone'


class RelentradaprodutofreteEntradaprodutofiscal(models.Model):
    tabentradaproduto_frete = models.ForeignKey('TabentradaprodutoFrete', models.DO_NOTHING,
                                                db_column='tabEntradaProduto_Frete_id')  # Field name made lowercase.
    tabentradaproduto_fiscal = models.ForeignKey('TabentradaprodutoFiscal', models.DO_NOTHING,
                                                 db_column='tabEntradaProduto_Fiscal_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relEntradaProdutoFrete_EntradaProdutoFiscal'


class RelentradaprodutoEntradaprodutofiscal(models.Model):
    tabentradaproduto = models.ForeignKey('Tabentradaproduto', models.DO_NOTHING,
                                          db_column='tabEntradaProduto_id')  # Field name made lowercase.
    tabentradaproduto_fiscal = models.ForeignKey('TabentradaprodutoFiscal', models.DO_NOTHING,
                                                 db_column='tabEntradaProduto_Fiscal_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relEntradaProduto_EntradaProdutoFiscal'


class RelentradaprodutoEntradaprodutofrete(models.Model):
    tabentradaproduto = models.ForeignKey('Tabentradaproduto', models.DO_NOTHING,
                                          db_column='tabEntradaProduto_id')  # Field name made lowercase.
    tabentradaproduto_frete = models.ForeignKey('TabentradaprodutoFrete', models.DO_NOTHING,
                                                db_column='tabEntradaProduto_Frete_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relEntradaProduto_EntradaProdutoFrete'


class RelprodutoCodbarra(models.Model):
    tabproduto = models.ForeignKey('Tabproduto', models.DO_NOTHING,
                                   db_column='tabProduto_id')  # Field name made lowercase.
    tabproduto_codbarra = models.ForeignKey('TabprodutoCodbarra', models.DO_NOTHING,
                                            db_column='tabProduto_CodBarra_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relProduto_CodBarra'


class Siscargo(models.Model):
    descricao = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'sisCargo'


class Sismenuprincipal(models.Model):
    descricao = models.CharField(max_length=45)
    titulotab = models.CharField(db_column='tituloTab', max_length=45, blank=True,
                                 null=True)  # Field name made lowercase.
    filho_id = models.IntegerField()
    icomenu = models.CharField(db_column='icoMenu', max_length=80, blank=True, null=True)  # Field name made lowercase.
    tabpane = models.IntegerField(db_column='tabPane')  # Field name made lowercase.
    teclaatalho = models.CharField(db_column='teclaAtalho', max_length=45, blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sisMenuPrincipal'


class Sismunicipio(models.Model):
    descricao = models.CharField(max_length=80)
    sisuf = models.ForeignKey('Sisuf', models.DO_NOTHING, db_column='sisUf_id')  # Field name made lowercase.
    iscapital = models.IntegerField(db_column='isCapital')  # Field name made lowercase.
    ibge_id = models.CharField(max_length=7)
    ddd = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sisMunicipio'


class Sissituacaosistema(models.Model):
    descricao = models.CharField(max_length=30)
    classificacao = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sisSituacaoSistema'


class Sisstatusnfe(models.Model):
    descricao = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'sisStatusNfe'


class Sistelefoneoperadora(models.Model):
    descricao = models.CharField(max_length=30)
    tipo = models.IntegerField()
    ddd = models.IntegerField()
    codwsportabilidadecelular = models.CharField(db_column='codWsPortabilidadeCelular', max_length=30, blank=True,
                                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sisTelefoneOperadora'


class Sistipoendereco(models.Model):
    descricao = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'sisTipoEndereco'


class Sisuf(models.Model):
    id = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'sisUf'


class Sisunidadecomercial(models.Model):
    descricao = models.CharField(max_length=30)
    sigla = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'sisUnidadeComercial'


class Tabcolaborador(models.Model):
    nome = models.CharField(max_length=80)
    apelido = models.CharField(max_length=30)
    senha = models.CharField(max_length=56)
    siscargo = models.ForeignKey(Siscargo, models.DO_NOTHING, db_column='sisCargo_id')  # Field name made lowercase.
    sissituacaosistema = models.ForeignKey(Sissituacaosistema, models.DO_NOTHING,
                                           db_column='sisSituacaoSistema_id')  # Field name made lowercase.
    tabloja = models.ForeignKey('Tabempresa', models.DO_NOTHING, db_column='tabLoja_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabColaborador'

    def autentica_login(self, usuario):
        colaborador = Tabcolaborador.objects.filter(apelido=usuario)
        if colaborador is not None:
            return colaborador
        else:
            return None

    def __str__(self):
        return self.apelido


class Tabcontato(models.Model):
    descricao = models.CharField(max_length=40)
    siscargo = models.ForeignKey(Siscargo, models.DO_NOTHING, db_column='sisCargo_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabContato'


class Tabemailhomepage(models.Model):
    descricao = models.CharField(max_length=80)
    isemail = models.IntegerField(db_column='isEmail')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabEmailHomePage'


class Tabempresa(models.Model):
    isempresa = models.IntegerField(db_column='isEmpresa')  # Field name made lowercase.
    cnpj = models.CharField(max_length=14)
    ieisento = models.IntegerField(db_column='ieIsento')  # Field name made lowercase.
    ie = models.CharField(max_length=14, blank=True, null=True)
    razao = models.CharField(max_length=80)
    fantasia = models.CharField(max_length=80)
    isloja = models.IntegerField(db_column='isLoja')  # Field name made lowercase.
    iscliente = models.IntegerField(db_column='isCliente')  # Field name made lowercase.
    isfornecedor = models.IntegerField(db_column='isFornecedor')  # Field name made lowercase.
    istransportadora = models.IntegerField(db_column='isTransportadora')  # Field name made lowercase.
    sissituacaosistema = models.ForeignKey(Sissituacaosistema, models.DO_NOTHING,
                                           db_column='sisSituacaoSistema_id')  # Field name made lowercase.
    usuariocadastro = models.ForeignKey(Tabcolaborador, models.DO_NOTHING, related_name='usuariodecadastro',
                                        db_column='usuarioCadastro_id')  # Field name made lowercase.
    datacadastro = models.DateTimeField(db_column='dataCadastro')  # Field name made lowercase.
    usuarioatualizacao = models.ForeignKey(Tabcolaborador, models.DO_NOTHING, db_column='usuarioAtualizacao_id',
                                           blank=True, null=True)  # Field name made lowercase.
    dataatualizacao = models.DateTimeField(db_column='dataAtualizacao', blank=True,
                                           null=True)  # Field name made lowercase.
    dataabertura = models.DateTimeField(db_column='dataAbertura', blank=True, null=True)  # Field name made lowercase.
    naturezajuridica = models.CharField(db_column='naturezaJuridica', max_length=150, blank=True,
                                        null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabEmpresa'


class Tabendereco(models.Model):
    sistipoendereco = models.ForeignKey(Sistipoendereco, models.DO_NOTHING,
                                        db_column='sisTipoEndereco_id')  # Field name made lowercase.
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=80)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=80)
    bairro = models.CharField(max_length=50)
    sismunicipio = models.ForeignKey(Sismunicipio, models.DO_NOTHING,
                                     db_column='sisMunicipio_id')  # Field name made lowercase.
    pontoreferencia = models.CharField(db_column='pontoReferencia', max_length=80)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabEndereco'


class Tabentradaproduto(models.Model):
    lojadestino = models.ForeignKey(Tabempresa, models.DO_NOTHING,
                                    db_column='lojaDestino_id')  # Field name made lowercase.
    chavenfe = models.CharField(db_column='chaveNfe', max_length=44)  # Field name made lowercase.
    numeronfe = models.IntegerField(db_column='numeroNfe')  # Field name made lowercase.
    serienfe = models.IntegerField(db_column='serieNfe')  # Field name made lowercase.
    modelonfe = models.ForeignKey(Fiscalmodelonfecte, models.DO_NOTHING,
                                  db_column='modeloNfe_id')  # Field name made lowercase.
    fornecedor = models.ForeignKey(Tabempresa, models.DO_NOTHING, related_name='fornecedor')
    dataemissaonfe = models.DateTimeField(db_column='dataEmissaoNfe')  # Field name made lowercase.
    dataentradanfe = models.DateTimeField(db_column='dataEntradaNfe')  # Field name made lowercase.
    statusnfe = models.ForeignKey(Sisstatusnfe, models.DO_NOTHING,
                                  db_column='statusNfe_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabEntradaProduto'


class TabentradaprodutoFiscal(models.Model):
    id = models.IntegerField(primary_key=True)
    numcontrole = models.CharField(db_column='numControle', max_length=13)  # Field name made lowercase.
    docorigem = models.CharField(db_column='docOrigem', max_length=12)  # Field name made lowercase.
    fiscaltributosefazam = models.ForeignKey(Fiscaltributosefazam, models.DO_NOTHING,
                                             db_column='fiscalTributoSefazAm_id')  # Field name made lowercase.
    vlrnfe = models.DecimalField(db_column='vlrNfe', max_digits=11, decimal_places=2)  # Field name made lowercase.
    vlrtributo = models.DecimalField(db_column='vlrTributo', max_digits=11,
                                     decimal_places=2)  # Field name made lowercase.
    vlrmulta = models.DecimalField(db_column='vlrMulta', max_digits=11, decimal_places=2)  # Field name made lowercase.
    vlrjuros = models.DecimalField(db_column='vlrJuros', max_digits=11, decimal_places=2)  # Field name made lowercase.
    vlrtaxa = models.DecimalField(db_column='vlrTaxa', max_digits=11, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabEntradaProduto_Fiscal'


class TabentradaprodutoFrete(models.Model):
    chavecte = models.CharField(db_column='chaveCte', max_length=44)  # Field name made lowercase.
    tomadorservico = models.ForeignKey(Fiscalfretetomadorservico, models.DO_NOTHING,
                                       db_column='tomadorServico_id')  # Field name made lowercase.
    numerocte = models.IntegerField(db_column='numeroCte')  # Field name made lowercase.
    seriecte = models.IntegerField(db_column='serieCte')  # Field name made lowercase.
    modelonfecte = models.ForeignKey(Fiscalmodelonfecte, models.DO_NOTHING,
                                     db_column='modeloNfeCte_id')  # Field name made lowercase.
    situacaotributaria = models.ForeignKey(Fiscalfretesituacaotributaria, models.DO_NOTHING,
                                           db_column='situacaoTributaria_id')  # Field name made lowercase.
    transportadora = models.ForeignKey(Tabempresa, models.DO_NOTHING)
    dataemissaocte = models.DateTimeField(db_column='dataEmissaoCte')  # Field name made lowercase.
    vlrcte = models.DecimalField(db_column='vlrCte', max_digits=11, decimal_places=2)  # Field name made lowercase.
    qtdvolume = models.IntegerField(db_column='qtdVolume')  # Field name made lowercase.
    pesobruto = models.DecimalField(db_column='pesoBruto', max_digits=11,
                                    decimal_places=2)  # Field name made lowercase.
    vlrfretebruto = models.DecimalField(db_column='vlrFreteBruto', max_digits=11,
                                        decimal_places=2)  # Field name made lowercase.
    vlrimpostofrete = models.DecimalField(db_column='vlrImpostoFrete', max_digits=11,
                                          decimal_places=2)  # Field name made lowercase.
    fiscal_cte_id = models.IntegerField(db_column='fiscal_Cte_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabEntradaProduto_Frete'


class Tabentradaprodutositens(models.Model):
    id = models.IntegerField(primary_key=True)
    tabentradaproduto = models.ForeignKey(Tabentradaproduto, models.DO_NOTHING,
                                          db_column='tabEntradaProduto_id')  # Field name made lowercase.
    tabproduto = models.ForeignKey('Tabproduto', models.DO_NOTHING,
                                   db_column='tabProduto_id')  # Field name made lowercase.
    codproduto = models.CharField(db_column='codProduto', max_length=15)  # Field name made lowercase.
    descricao = models.CharField(max_length=120)
    peso = models.DecimalField(max_digits=11, decimal_places=3)
    qtd = models.IntegerField()
    vlrfabrica = models.DecimalField(db_column='vlrFabrica', max_digits=11,
                                     decimal_places=2)  # Field name made lowercase.
    vlrtotalbruto = models.DecimalField(db_column='vlrTotalBruto', max_digits=11,
                                        decimal_places=2)  # Field name made lowercase.
    vlrimposto = models.DecimalField(db_column='vlrImposto', max_digits=11,
                                     decimal_places=2)  # Field name made lowercase.
    vlrdesconto = models.DecimalField(db_column='vlrDesconto', max_digits=11,
                                      decimal_places=2)  # Field name made lowercase.
    vlrliquido = models.DecimalField(db_column='vlrLiquido', max_digits=11,
                                     decimal_places=2)  # Field name made lowercase.
    estoque = models.IntegerField()
    varejo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tabEntradaProdutosItens'


class Tabinformacaoreceitafederal(models.Model):
    isatividadeprincipal = models.IntegerField(db_column='isAtividadePrincipal')  # Field name made lowercase.
    str_key = models.CharField(db_column='str_Key', max_length=70)  # Field name made lowercase.
    str_value = models.CharField(db_column='str_Value', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabInformacaoReceitaFederal'


class Tabproduto(models.Model):
    codigo = models.CharField(max_length=15)
    descricao = models.CharField(max_length=120)
    peso = models.DecimalField(max_digits=9, decimal_places=3)
    sisunidadecomercial = models.ForeignKey(Sisunidadecomercial, models.DO_NOTHING,
                                            db_column='sisUnidadeComercial_id')  # Field name made lowercase.
    sissituacaosistema = models.ForeignKey(Sissituacaosistema, models.DO_NOTHING,
                                           db_column='sisSituacaoSistema_id')  # Field name made lowercase.
    precofabrica = models.DecimalField(db_column='precoFabrica', max_digits=11,
                                       decimal_places=2)  # Field name made lowercase.
    precovenda = models.DecimalField(db_column='precoVenda', max_digits=11,
                                     decimal_places=2)  # Field name made lowercase.
    varejo = models.IntegerField()
    precoultimoimpostosefaz = models.DecimalField(db_column='precoUltimoImpostoSEFAZ', max_digits=11,
                                                  decimal_places=2)  # Field name made lowercase.
    precoultimofrete = models.DecimalField(db_column='precoUltimoFrete', max_digits=11,
                                           decimal_places=2)  # Field name made lowercase.
    comissao = models.DecimalField(max_digits=11, decimal_places=2)
    ncm = models.CharField(max_length=8, blank=True, null=True)
    cest = models.CharField(max_length=7, blank=True, null=True)
    fiscalcstorigem = models.ForeignKey(Fiscalcstorigem, models.DO_NOTHING,
                                        db_column='fiscalCstOrigem_id')  # Field name made lowercase.
    fiscalicms = models.ForeignKey(Fiscalicms, models.DO_NOTHING,
                                   db_column='fiscalIcms_id')  # Field name made lowercase.
    fiscalpis = models.ForeignKey(Fiscalpiscofins, models.DO_NOTHING,
                                  db_column='fiscalPis_id')  # Field name made lowercase.
    fiscalcofins = models.ForeignKey(Fiscalpiscofins, models.DO_NOTHING, related_name='fiscalcofins',
                                     db_column='fiscalCofins_id')  # Field name made lowercase.
    nfegenero = models.CharField(db_column='nfeGenero', max_length=10)  # Field name made lowercase.
    usuariocadastro = models.ForeignKey(Tabcolaborador, models.DO_NOTHING,
                                        db_column='usuarioCadastro_id')  # Field name made lowercase.
    datacadastro = models.DateTimeField(db_column='dataCadastro')  # Field name made lowercase.
    usuarioatualizacao = models.ForeignKey(Tabcolaborador, models.DO_NOTHING, related_name='usuarioatualizacao',
                                           db_column='usuarioAtualizacao_id', blank=True,
                                           null=True)  # Field name made lowercase.
    dataatualizacao = models.DateTimeField(db_column='dataAtualizacao', blank=True,
                                           null=True)  # Field name made lowercase.
    imgproduto = models.TextField(db_column='imgProduto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabProduto'


class TabprodutoCodbarra(models.Model):
    codbarra = models.CharField(db_column='codBarra', max_length=13)  # Field name made lowercase.
    imgcodbarra = models.TextField(db_column='imgCodBarra', blank=True, null=True)  # Field name made lowercase.
    oioioi = models.CharField(db_column='OIOIOI', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabProduto_CodBarra'


class TabprodutoEstoque(models.Model):
    produto = models.ForeignKey(Tabproduto, models.DO_NOTHING)
    qtd = models.IntegerField()
    lote = models.CharField(max_length=20)
    validade = models.DateTimeField()
    vlrbruto = models.DecimalField(db_column='vlrBruto', max_digits=11, decimal_places=2)  # Field name made lowercase.
    vlrimposto = models.DecimalField(db_column='vlrImposto', max_digits=11,
                                     decimal_places=2)  # Field name made lowercase.
    vlrfrete = models.DecimalField(db_column='vlrFrete', max_digits=11, decimal_places=2)  # Field name made lowercase.
    vlrfreteimposto = models.DecimalField(db_column='vlrFreteImposto', max_digits=11,
                                          decimal_places=2)  # Field name made lowercase.
    vlrfreteliquido = models.DecimalField(db_column='vlrFreteLiquido', max_digits=11,
                                          decimal_places=2)  # Field name made lowercase.
    vlrliquido = models.DecimalField(db_column='vlrLiquido', max_digits=11,
                                     decimal_places=2)  # Field name made lowercase.
    usuariocadastro = models.ForeignKey(Tabcolaborador, models.DO_NOTHING,
                                        db_column='usuarioCadastro_id')  # Field name made lowercase.
    datacadastro = models.DateTimeField(db_column='dataCadastro')  # Field name made lowercase.
    docorigem = models.CharField(db_column='docOrigem', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.
    chavenfeentrada = models.CharField(db_column='chaveNfeEntrada', max_length=44, blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabProduto_Estoque'


class Tabtelefone(models.Model):
    descricao = models.CharField(max_length=11)
    sistelefoneoperadora = models.ForeignKey(Sistelefoneoperadora, models.DO_NOTHING,
                                             db_column='sisTelefoneOperadora_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabTelefone'
