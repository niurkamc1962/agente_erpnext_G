Módulo Cuba RRHH. Nómina

2026

**Índice**

1.  Generalidades……………………………………………………………………......4

.

1.  Pasos a seguir para la configuración………………………………………..….….4

2.1.- Definir las cuentas asociadas y otras configuraciones en HR y Nómina……………………………………………………………………….…….…4

2.2.- Configurar particularidades del proceso para Cuba……………………...6

2.3.- Configurar Lista de festividades…………………………………….……..…9

2.4.- Configurar los Departamentos……………………………………….10

2.5.- Configurar Tipo de Turnos……………………………………………………11

2.6.- Configurar Esquemas de Turnos Rotativo……………………………...….12

2.7.- Configurar Recursos Humanos…………………………………….………..14

2.7.1.- Definir Nomenclador Nivel Educacional……………………….……15

2.7.2.- Definir Nomenclador Categoría Ocupacional……………………...16

2.7.3.- Definir Grupos Salariales…………………………………………….16

2.7.4.- Definir Puestos (Cargos)……………………………………………..16

2.7.5.- Definir Puesto de trabajo…………………………………….……….18

2.8.- Agregar Empleado…………………………………………………….……..19

2.9.- Apertura de Submayor de vacaciones…………………………….……….23

III. Configurar la Nómina de Sueldo

3.1.- Configurar Nómina………………………………………………………..….25

3,2.- Definir Componentes Salariales………………………………………….…26

3.3.- Definir Esquema Salarial ……………………………………………..…..…29

3.4.- Asignar Esquema Salarial a los Empleados……………………………….31

3.5.- Agregar Pago Adicional. (Salario Adicional) ……………………………….32

3.5.1 Tipo de Salario Adicional ………………………………………………32

3.5.2 Agregar Salario Adicional………………………………………………33

3.6.- Definir Tipos y Políticas de licencias……………………………………… 34

3.6.1.- Tipo de licencias……………………………………………………….34

3.6.2.- Política de Licencias…………….……………………………………35

3.6.3.- Asignación de licencias a los Empleados……..…………………….35

IV.- Procesar la Nómina………………………………………………..….36

4.1.- Abrir Período de Nómina………………………………….………………....36

4.2.- Registrar Licencias y Asistencia del Empleado……….……………...…...36

4.2.1.- Solicitud de Licencia………………………………………………....37

4.2.2.- Marcar Asistencia………………………………………………….…39

4.3.- Entrada de nómina…………………………………………………………. ..41

4.4.- Recibos de Salario (Salary Slip) ……………………………….……………44

4.5.- Liquidación de Nómina………………………………………………………..45

4.6.- Cerrar Período…………………………………………………………………45

4.6.1 Verificar escritura en SC- 408………………………………………….46

V- Otros Procesos………………………………………………………………………..46

5.1.- Ajuste del Submayor de vacaciones…………………………………………46

5.2.- Retenciones……………………………………………………………………..47

5.2.1 Tipo de Retenciones……………………………………………………..47

5.2.2 Maestro de Retenciones…………………………………………………48

5.3.- Pensionadas…………………………………………………………………….49

5.4.- Salarios No Reclamados……………………………………………………….50

5.4.1 Apertura del Submayor de Salario No Reclamado……………………

5.4.2 Submayor de Salarios No Reclamados………………………………..

**I.- Generalidades.**

En este documento abarcaremos las particularidades del proceso de Nómina en ERPNext para el entorno cubano. Para operar en este entorno se debe acceder a las _Configuraciones de Dominio_ y marcar el Dominio HR Cuban Enviroment:

Para cubrir todo el proceso de nómina se debe acceder a las opciones del Menú: _Cuba HR y Nóminas de Sueldo._

**II. Pasos a seguir para la realizar la configuración.**

Definir las cuentas asociadas y otras configuraciones en HR y Nómina.

_Contabilidad/ Compañía/ HR & Nómina de Sueldos_

Detalles:

- **Cuenta nómina predeterminada de la cuenta por pagar**, es la cuenta donde al procesar la nómina, el sistema acredita y debita los gastos de salario.

- **Cuenta predeterminada de anticipo de empleado,** registrarán los anticipos que la empresa le otorga a los empleados (ejemplo las dietas, pagos menores)

_Contabilidad/ Compañía/ Cuba_

2.2 - Configurar particularidades del proceso para Cuba.

_Cuba HR/ Configuración de Cuba_

- Pestaña _Empleados_

Seleccionar los campos según la necesidad del usuario. Pestaña _Asistencia_

Seleccionar los campos según la necesidad del usuario

- Pestaña _Licencia_

- Pestaña _Vacaciones_

- Pestaña _Nómina de Sueldo_

- Pestaña _Evaluación_

- Pestaña _Operación._

Se utiliza para las formas de pago a rendimiento: Destajo Individual y Destajo Indirecto.

- Pestaña _Producción Diaria._

Se utiliza para las formas de pago a rendimiento: Destajo Individual y Destajo Indirecto.

- Pestaña _Informes_

2.3.- Configurar Lista de festividades.

_Lista de Vacaciones/ Agregar Lista_

Se deben definir los días de receso laboral y festividades a nivel de Compañía, se pueden personalizar para grupo de Empleados o a nivel de un empleado específico.

2.4 – Definir los Departamentos.

_Departamento/Agregar departamento_

Para visualizar la estructura se recomienda la Vista de Árbol. Se define la estructura organizativa de la compañía con sus niveles jerárquicos, cada nivel debe establecerse como _Grupo_ hasta tanto se llegue al último nivel deseado

Se debe seleccionar el Centro de costo correspondiente, donde se registrará el gasto de la nómina. Se deben definir las personas que aprueban, el primero que aparezca en la lista será el predeterminando.

2.5- Configurar Tipo de Turnos.

_Cuba HR/Tipo de Turnos/Agregar Turno_

Se definen los tipos de turno según las horas de trabajo, horas de inicio y fin.

2.6.- Configurar Esquemas de Turnos Rotativos.

_Cuba HR/Esquema de Turnos rotativos/Nuevo Esquema_

Los esquemas de turnos rotativos pueden ser: semanal, continuos y diferenciados.

- **Semanal.** Se establece el comportamiento semanal y puede ser diferente para cada día de la semana, configurando el _Tipo de turno_ para cada día, como se muestra a continuación:

- **_Turno Continuo._** Se deben definir los días de trabajo y días de descanso.

- **_Turno Diferenciado_**

Al asignarlo, hay que definir los turnos de trabajo por día. Los asigna mes a mes, si dado el caso se cambia la asignación, se desactiva la anterior y se activa la nueva. Para lograr ésto hay que habilitar la casilla Allow Multiple Shift Assigments for same date, en la configuración de HR

2.7- Configurar Recursos Humanos

_HR/ Configuración de Recursos Humanos_

**Nombre del Empleado por.** Se utiliza para determinar el campo por el que se identifica el empleado. Puede seleccionar las siguientes opciones:

\* Secuencias e identificadores. (Previamente definido en la configuración de nombre de documentos/Empleado).

\* Número de empleado.

\* Nombre Completo.

**Horas de trabajo estándar.** Es un dato requerido y se utiliza para calcular el coeficiente salarial del empleado para gestionar el salario nominal.

;

**Recordatorio**: Se envía mensaje según los eventos seleccionados, al correo electrónico identificado en **_Remitente_** con la frecuencia seleccionada**.**

**Edad de jubilación** - se sugiere no completar, puesto que para Cuba es diferente según el género.

**Otras configuraciones**:

Si utiliza esquema de turnos al marcar esta opción le facilita el marcaje de asistencia en un rango de fecha con diferentes turnos.

2.7.1 - Definir nomenclador de Nivel educacional

_Cuba HR/ Nivel educacional_

2.7.2.- Definir Nomenclador de Categoría Ocupacional

_Cuba HR/Categoría Ocupacional/ Agregar Nuevo_

2.7.3.- Definir Nomenclador de Grupo Salarial.

_Cuba HR//grupo de Salario/Agregar Nuevo_

Se define el Grupo Salarial con sus datos asociados: salario, categoría ocupacional y nivel educacional.

2.7.4 - Definir los Puestos (cargos).

_Puesto/ Agregar Puesto_

Para cada cargo de la compañía se le puede definir un objetivo o misión, asociarle una Plantilla de evaluación (previamente diseñada) y las habilidades requeridas.

Ejemplo de Puesto:

2.7.5 – Definir los Puestos de Trabajo.

El Puesto de trabajo es el puesto que se asocia al trabajador de un departamento, debe definir un código, seleccionar el Puesto (cargo), el Grupo de Salario y el Departamento al que pertenece. Con esos datos se identificará el puesto de trabajo específico.

Ejemplo de Puestos de Trabajo.

Note que el identificador del Puesto de trabajo es la concatenación de: _Código-Departamento-Puesto_

2.8.- Agregar Empleado (también se puede realizar a través de la importación de datos en la carga inicial).

- Pestaña Descripción General

- Pestaña Union.

Se muestran y completan datos asociados al proceso de reclutamiento (si procede), fin del contrato y jubilación.

- Pestaña Dirección y contactos.

- Pestaña Asistencia y licencias.

Si la asistencia se registra a través de un dispositivo externo se debe especificar el ID correspondiente. Se debe seleccionar la lista de festividades previamente configurada y el turno predeterminado para el empleado (si procede, si tiene turno rotativo no se selecciona)

- Pestaña Salario.

Se debe especificar la moneda de pago, el modo de pago: _Efectivo, Banco, Cheque_ y el centro de costo donde se cargará el gasto de salario. En el caso de seleccionar **_Banco_** debe detallar el _Nombre del Banco_ y el _número de cuenta bancaria_.

- Pestaña Personal.

Ninguno de los datos en esta pestaña es obligatorios. Se puede introducir el estado Civil, Grupo sanguíneo, otros detalles de salud y antecedentes familiares que sean de interés de la Compañía, así como los datos asociados al pasaporte.

- Pestaña Perfil.

En esta pestaña se puede especificar una breve biografía del empleado, incluyendo su Formación Académica y Experiencia Laboral previa. La sección de _Historía en la Compañía se irá completando en la medida que el empleado transite por la compañía._

- Pestaña Conexiones/Otras Informaciones

En esta pestaña se definen las particularidades del trabajador en cuanto a las vacaciones: _No Acumula, Acumula y disfruta, Acumula y No disfruta_; el Tipo de pago, Grupo salarial, Categoría ocupacional, nivel de escolaridad y puesto de trabajo, la pertenencia a un grupo de empleados (si se ha definido).

- Pestaña Salir (baja)

En esta pestaña se registra la información referente al proceso de baja del empleado, la fechas de solicitud de baja , fecha prevista de salida efectiva, se puede especificar si las vacaciones ya fueron liquidadas y las causas de la baja.

**2.9- Submayor de vacaciones.**

2.9.1.- Aperturar el submayor de Vacaciones.

Esta opción se utiliza para actualizarle a cada trabajador los días e importes acumulados de vacaciones antes de comenzar a calcular la primera nómina por el sistema.

Prerrequisitos.

- Debe definir la cuenta de Provisión de Vacaciones en _Compañía/_ pestaña HR/ Nomina.
- Debe definir una cuenta contrapartida de Tipo Temporal para usarla en el asiento de apertura de la Provisión de vacaciones:

Cuba HR/ Configuración de Cuba, pestaña Contabilidad

- - 1.  Actualizar el saldo de la cuenta de Provisión de Vacaciones.

_Asiento contable//nuevo_

Debe seleccionar Tipo de entrada: **_Asiento de apertura._** _Seleccionar la cuenta de provisión de vacaciones y la contrapartida._

Después de validar el asiento se habilita la opción Close Opening Entry y al seleccionarlo queda cerrada la apertura.

2.9.3.- Aperturar el acumulado de vacaciones de cada trabajador.

_Cuba HR/Apertura del Submayor de vacaciones del Empleado_

En la selección de los empleados, aparecerán solamente los empleados activos y que tengan configurado que _disfrutan y acumulan vacaciones_.

III – Nómina de Sueldo

3.1.- Configurar Nómina.

_Nómina de Sueldo / Configuración de Nómina_

Si desea que se muestre el asiento contable con el detalle de cada empleado debe marcar el campo _Procesar Asiento Contable de Nómina Basado en empleado_.

3.2. - Definir los Componentes salariales.

Los componentes salariales permiten desglosar los distintos conceptos que conforman el salario, pueden ser de ingreso o deducciones. Es imprescindible definirlos todos para garantizar su contabilización, tanto los que se gestionan a través de políticas y licencias: Vacaciones, licencias de maternidad pre y posnatal, prestación social, certificados médicos e interrupciones laborales, como los que se definen por fórmula: Salario escala, conceptos de pago y pagos adicionales, así como las contribuciones e impuestos.

**Tipos de Componentes salariales:**

- De ingreso: Salario Escala, Vacaciones, Maestría, Certificados médicos, Pago adicional, conceptos de pago, etc.
- De deducciones son: Impuestos Seguridad Social a corto y largo plazo y contribución especial, Impuestos sobre ingresos personales, etc.

**Características de los componentes salariales (CS):**

- Para cada CS se define la cuenta en la que se va a contabilizar el resultado del cálculo y la forma de cálculo del mismo para aquellos conceptos que se define por fórmula.
- En el CS se define si es de ingreso o deducción.
- El comportamiento de cada CS define en cuál columna de la nómina estará el resultado del cálculo de ese componente. Los valores pueden ser:

- - Salario Escala
    - Conceptos de Pago
    - Pagos adicionales
    - Vacaciones
    - Certificado Médico
    - Licencia de Maternidad
    - Beneficio Social
    - CESS
    - ISSIP
    - Retenciones
    - Otros

- A cada CS se le asocia la cuenta donde se contabilizará, si es una cuenta que se abre por elemento de gasto se definirá el elemento de gasto.

- El resto de las casillas se marcarán según las características del CS.

- La casilla _Componente estadístico_ se marca para aquellos componentes que se utilizarán en la fórmula de cálculo de otros componentes, y no contribuirá ni a ingresos ni a deducciones. Ej: Fondo de Tiempo

_Nómina de Sueldos/Componte Salarial/Agregar Nuevo_

**Ejemplo de Componente Salarial. Salario Escala**

- **Pestaña. Descripción General.**

- **Pestaña. Condición y Fórmula**

- **Pestaña Promedios y SC-4-08**

Todos los componentes y su comportamiento se pueden introducir en el sistema a través del proceso de importación previsto en ERPNext previa preparación de la plantilla correspondiente.

3.3.- Definir Estructura Salarial.

La estructura salarial es lo que se le asigna al empleado para definirle la composición de su salario y agrupar los componentes salariales definidos anteriormente.

Se deben crear tantas estructuras salariales como se necesiten, tratando de agrupar en una estructura los conceptos que serán utilizados por la mayoría de los empleados. Una misma estructura se le puede asignar a varios empleados.

**Ejemplo Estructura para Salario básico.**

_Nómina de Sueldo/ Estructura salarial_

- _Pestaña Detalles_

En la estructura se define la frecuencia de pago: Diario, Semanal, Quincenal, Mensual, Bimensual, Trimestral.

El campo **_Nómina basado en horas_**, se debe marcar sólamente cuando el cálculo de las horas se realiza a través de las funciones de Proyecto y/o Manufactura.

- _Pestaña Ganancias y Deducciones_

En las tablas se adicionan todos los componentes que conformarán la estructura salarial según sea el caso: Ganancias o Deducciones, debiendo añadirlo a la lista en el orden en que se ejecuta el cálculo de los diferentes conceptos.

- Ejemplos de Estructura Salarial.

3.4 - Asignación de la Estructura salarial a los Empleados.

Para asignar la estructura a un Empleado específico:

_Nómina de Sueldos/Asignación de Estructura salarial/Agregar Asignación_

En caso de que desee asignar una misma estructura salarial a varios empleados:

_Nómina de Sueldos/ Estructura salarial_

Debe seleccionar el botón _Bulk Salary Structure Assignment, en la siguiente pantalla seleccionar la estructura y marcar los empleados a los que desee asignársela._

3.5.- Agregar pagos adicionales. (Salario adicional)

El salario adicional se utiliza para realizar un pago puntual al trabajador o para aplicar un pago durante un período de tiempo (marcar recurrente), en cuyo caso deben establecerse el rango de fecha durante el cual se realizarán los pagos.

Para agregar un pago adicional debe crearse previamente un componente salarial (acápite 2.15) que lo defina y establecer los Tipos de Salario Adicional.

3.5.1- Tipo de Salario Adicional

Cuba HR/ Tipo de Salario Adicional/ Agregar Nuevo

Los tipos de salario adicional se definen según el comportamiento de su escritura en el SC-408 y su participación en la base de cálculo para el cálculo de los promedios.

- Forma de escritura en el SC- 408: _Real Pagado, Salario básico, No se anota_.
- Forma parte de la base de cálculo de promedios: Todos, Ninguno, sólo subsidios, excluye subsidios.

3.5.2- Agregar Salario Adicional

_Nómina de Sueldo/ Salario adicional/Agregar_

El componente definido como _Pago adicional_ no se agrega por el usuario al crear la estructura salarial, pero al asignarlo al trabajador el sistema lo incorpora en la estructura para calcular la nómina en el período que corresponda (debe marcar _Sobrescribir el monto de la estructura salarial). Si desea que ese pago se incluya en el cálculo de las interrupciones debe marcarlo también_

3.6.- Definir Tipos de licencias y política de licencias.

En ErpNext los días que no se registran como asistencia se deben tipificar como licencias: Vacaciones, Licencias de Maternidad, Licencias sin sueldo, Certificado Médico, interrupciones, etc.

3.6.1- Tipo de Licencias

_HR Cuba/Tipo de Licencia_

Para cada Tipo de Licencias se debe definir:

- **Límites de días** (máximo por año).
- **Si permite sobrepasar el límite definido**
- **Concepto: vacaciones, interrupción laboral, licencia de maternidad, etc.**

además, se debe completar toda la información que se define en el componente salarial (excepto las cuentas), pues desde aquí el sistema se alimenta para realizar los cálculos:

- Si acumula vacaciones
- Si aplica los diferentes impuestos
- **Forma de escritura en el SC-408**

.**Ejemplo de Tipo de Licencia**: _Vacaciones_

3.6.2.- Políticas de licencias:

En la Política de licencias se quedará reflejada, la asignación anual permisible de cada tipo de licencia, se puede agrupar varios tipos.

3.6.3.- Asignación de política de licencias a los Empleados.

_HR / Asignación de vacaciones_

Note que en ERpNext el término _vacaciones_ se utiliza indistintamente para referirse a todas las licencias o para el tipo de licencia _vacaciones_ en específico.

4.- Proceso de Nómina.

4.1.- Definir Período de Nómina.

Antes de comenzar a registrar la asistencia, licencias, etc. y realizar la Entrada de Nómina debe abrirse el Período de Nómina que corresponde.

_Nómina de sueldo/ Período de Nómina /Nuevo_

Validaciones que se realizan:

No debe existir ningún otro período abierto. La fecha de inicio del nuevo período debe ser consecutiva a la Fecha final del período anterior. La fecha final del nuevo período debe estar en el mismo mes de la fecha de inicio y dependerá de la frecuencia de la nómina (Mensual, Quincenal).

Al presionar el botón Guardar, si todo está correcto se mostrará el nuevo periodo en Estado **_Abierto._**

4.2. Registro de Licencias y Asistencia del Empleado.

ERPNext centraliza la gestión de asistencia y licencias en un sólo lugar, con opciones para :

- Registro manual o automático (si tiene acoplado algún dispositivo de control de presencia)
- Solicitudes y aprobaciones según los roles y permisos establecidos.

Se deben registrar primeramente las licencias y posteriormente la asistencia. Si un empleado solicita una licencia y es aprobada, automáticamente se marca su asistencia como **"On Leave"** en ese día.

Las ausencias no justificadas (sin registro de asistencia ni licencia) pueden identificarse en informes como **Missing Attendance Report**.

4.2.1.- Registrar Licencias.

HR/ Solicitud de Licencia/Nuevo

En **_Tipo de licencia_** se mostrarán los Tipos de licencias definidas ,asignadas al empleado en correspondencia con la fecha calendario.

Según el Tipo de licencia se mostrarán los campos a completar y se realizarán las validaciones correspondientes.

En el campo **_Aprobación_** se selecciona el empleado con el rol de supervisor que tiene los permisos para aprobar la solicitud. Para dar seguimiento por correo electrónico debe marcar la casilla correspondiente.

En el campo **_Fecha de publicación_** se muestra la fecha actual.

El campo **_Estado_** se inicia con **_Abierto_** y cambiará cuando sea aprobada la solicitud.

**Ejemplo Certificado Médico**:

Para este caso se valida que la **_fecha desde_** y **_hasta_** esté enmarcada en el mes anterior y posterior a la fecha en que se capta la licencia.

4.2.2. - Marcar Asistencia.

Se puede marcar la asistencia de un empleado en un día específico del mes:

_HR/Asistencia/Nuevo_

Para actualizar la asistencia de un empleado en un rango de fecha: debe seleccionar la opción _Marcar asistencia_

_HR/ Asistencia_

Al marcar la opción se mostrará la siguiente pantalla:

Debe seleccionar el Empleado y definir las fechas de Inicio y Fin. El sistema sólo permite seleccionar las fechas inferiores a la fecha actual, por lo que no podrá completar la asistencia de los días que aún no han transcurrido (no permite adelantar cierre de asistencia).

Tenga en cuenta que la fecha de inicio debe coincidir con el día de la semana del turno que desee actualizar, de lo contrario no se le mostrará el turno de trabajo para seleccionar.

Se mostrarán los días que aún no tienen marcada ninguna incidencia, debiendo marcar las que procedan según el Estado que desea actualizar: Presente, ausente, medio día, etc. Así como actualizar el turno que corresponda.

Se sugiere marcar la casilla de excluir vacaciones para que sólo muestre los días laborables del rango de fecha seleccionado.

4.3.- Entrada de nómina o nómina salarial.

Detalle Importante a verificar:

Se recomienda verificar que cada empleado en su configuración, tenga correctamente definido el modo de pago:

. 

En dependencia del modo de pago será el comportamiento del proceso de liquidación de nómina. Ver acápite _4.5. Liquidación de Nómina_.

Para realizar la nómina se deben tener, para los días del período de nómina abierto: todas las licencias aprobadas y la asistencia de los empleados (el resto de los días que falten se considerará ausencias).

_Nómina de Sueldos / Entrada de Nómina\\_

Pestaña Visión General.

Detalles:

- Fecha de publicación: Es el último día del mes del período de la nómina que se va a calcular. **_Este campo debe llenarse de primero para que se complete correctamente la fecha de inicio y fin de la nómina._**

- Período de nómina. Se mostrará sólo el activo.

- Fecha de inicio y Fin. Se completará según período seleccionado.

.

_Pestaña Contabilidad y Pago._

Al completar el resto de los datos y guardar aparecerá un botón de empleados para seleccionar los Empleados a los que se le realizará la nómina: Al dar click en el botón, se listarán los empleados que cumple con la frecuencia de la nómina y la estructura de salarial válida entre la fecha de inicio y fin de esa nómina.

Nota: No necesariamente hay que habilitar el pago para todos los empleados, se pueden dejar sin habilitar los empleados que correspondan.

Aparecerá el botón de crear Recibos de sueldo y le crea a cada empleado su nómina salarial.

4.4. Recibo de Salario.

Al entrar a un recibo de salario se pueden verificar todos los cálculos realizados.

Recibo de Salario /Pestaña Cuba:

Al Validar los recibos de Salario, el estado de la Entrada de Nómina cambia a _Enviada_ y crea en automático el asiento contable para contabilizar la nómina. Si todos los trabajadores tienen modo de pago Banco, el estado de la entrada de nómina pasa directamente a _Liquidada._

4.5 Liquidación de Nómina.

_Cuba HR/Liquidación de nóminas._

Esta opción sólo procede utilizarla cuando alguno de los empleados incluidos en la entrada de nómina tiene seleccionado el modo de pago diferente a _Banco_.

Se selecciona la entrada de nómina y el resto de los filtros que propone la vista, se mostrarán los empleados que no tenían el modo de pago _Banco_ y se presiona el botón _Liquidar_. El sistema muestra el mensaje: “ _las nóminas han sido liquidadas correctamente” y la_ Entrada de Nómina pasa a estado _Liquidada._

**Importante**: Si todos los empleados tienen el modo de pago _Banco,_ la entrada de nómina pasará directamente a estado _Liquidada_ y esta opción no se utiliza.

4.6 Cerrar Período de nómina.

Nómina de sueldos/ Período de nómina.

Se cierra el período de nómina y se valida que no existan entradas de nóminas pendientes en el proceso de gestión.

En este proceso se realiza de forma automática la escritura en el SC- 408 Registro de Salario y tiempo de Servicio de cada empleado, del tiempo e importe devengado.

4.6.1 Verificar escritura en SC- 408.

Posterior al Cierre de Período se verifican los datos registrados en el SC-4-08 y muestra el enlace del salario slip correspondiente.

V- Otros Procesos.

5.1.- Ajuste del Submayor de vacaciones.

- Permite la selección de los empleados que tienen configurado que acumulan y disfrutan vacaciones.
- Se pueden realizar ajustes tanto en días como en importe.

5.2.- Retenciones.

5.2.1 Tipo de Retenciones.

5.2.2 Maestro de Retenciones.

5.3. Pensionadas.

5.4. Salarios No Reclamados.

5.4.1 Apertura del Submayor de Salarios No Reclamados

5.4.2 Submayor de Salarios No Reclamados