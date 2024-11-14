import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")

sheet_id: str = "1yvnpNM3JGI8YhN80RlCKD1VmbSmRs5umSfzMl_n8Rpw"
sheet_url: str = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
raw_data = pd.read_csv(sheet_url)
raw_data.drop(axis=1, labels=["TOTAL HS", "Total"], inplace=True)
data = raw_data.drop(axis=1, labels=[col for col in raw_data.columns if col.endswith('%')])

left, right = st.columns(2)

with right:
	with st.container(border=True):
		ileft, ileft2, _, _ = st.columns(4)
		with ileft:
			st.metric(
				'Total de horas invertidas (aprox.)',
				f'~{data.sum(numeric_only=True).sum() * 6:.1f}'
			)
		with ileft2:
			st.metric('Meses trabajados (aprox.)', 6)
		
		fig = px.bar(
			data.sort_values('Producto', ascending=False),
			['Investigación', 'Desarrollo', 'Bug fixing', 'Testing', 'Despliegue'],
			'Producto', text_auto=True
		)
		fig.update_layout(
			title='~ Distribución hs/mes invertidas x Producto x Categoría',
			xaxis_title='',
			yaxis_title='',
			xaxis={"showticklabels": False},
			legend_title='Categorías'
		)
		st.plotly_chart(fig)
		
		summed_categories = data.sum(numeric_only=True)
		fig = px.bar(
			summed_categories, color_discrete_sequence=px.colors.qualitative.Pastel,
			text_auto=True
		)
		fig.update_layout(
			title='~ Promedio de hs/mes invertidas x Categoría',
			xaxis_title='',
			yaxis_title='',
			showlegend=False
		)
		st.plotly_chart(fig)

with left:
	st.header('Lista de :orange[productos] y tareas realizadas:')
	
	ileft, icenter = st.columns(2)
	
	with ileft:
		st.markdown(
			"""
					- **:orange[Base de Datos]**:
						- _:gray[Versión 1]_:
							1. Optimización de _:red[algorítmos de búsqueda]_.
							2. Creación y relación de modelos previamente inexistentes.
						- _:violet[Versión 2]_:
							1. Migración (con fines de optimización y desarrollo del **:orange[
						Dashboard V2]**).
						- _:blue[Versión 3]_ (En desarrollo):
							1. Migración (con fines de optimización e implementación de pedidos)
					- **:orange[API]**:
						- _:gray[Versión 1]_:
							1. Optimización.
							2. Optimización de _:red[algorítmos de búsqueda]_.
							3. Limpieza de código en desuso.
						- _:violet[Versión 2]_:
							1. Migración.
							2. Adaptación de _:red[algorítmos de búsqueda]_ para encajar con la _:violet[
							Versión 2]_.
						- _:blue[Versión 3]_ (En desarrollo):
							1. Investigación exhaustiva y elección del [Stack Tecnológico](https://shorturl.at/wKZRZ) que se
							implementaría durante el desarrollo.
							2. Desarrollo desde 0.
							3. Migración de Base de Datos.
					"""
		)
	
	with icenter:
		st.markdown(
			"""
					- **:orange[Dashboard]** (Previamente se utilizaba un
							link de Google Sheets que debía ser actualizado manualmente por :green[HelpHub]):
						- _:gray[Versión 1]_:
							1. Investigación exhaustiva y elección del [Stack Tecnológico](https://shorturl.at/wKZRZ) que se
							implementaría durante el desarrollo.
							2. Diseño y desarrollo a partir de la **:orange[API V2]**.
							3. Optimización [UX](https://rockcontent.com/es/blog/ui-ux/).
						- _:violet[Versión 2]_ (En desarrollo):
							1. Migración de la **:orange[API V3]**:
							2. Desarrollo desde 0.
							3. Despliegue (debido a la migración llevó varios días de trabajo y solución de
							errores).
					- **:orange[ChatBot]**:
						1. Personalización
						2. Humanización
					- **:orange[Integración]** (Simplificación de actualizaciones con respecto a las
					versiones de la **:orange[API]**):
						1. Investigación.
						2. Desarrollo.
						3. Debugging.
						4. Despliegue.
						5. Implementación en el **:orange[ChatBot]**.
					- **:orange[Pedidos]**:
						1. **:orange[Dashboard]**:.
						2. Humanización del ChatBot.
						3. Múltiples ChatBots (En pausa).
					"""
		)
	
	st.divider()
	
	ileft, icenter, iright = st.columns(3)
	
	with ileft:
		with st.expander(':blue[Propuesta 1]'):
			st.metric('Monto (USD)', '$450', delta="$350", delta_color='off')
	
	with icenter:
		with st.expander(':green[Propuesta 2]'):
			st.metric('Monto (USD)', '$650', delta="$550", delta_color='off')
			st.markdown("""
			:green[+ Implementación de pedidos personalizados (ej: alertas personalizadas)]\n
			:green[+ Desarrollo de ChatBots con otras tareas (ej: seguimiento de envíos)]
			""")
	
	with iright:
		with st.expander(':gray[Propuesta 3]'):
			st.markdown('Estamos abiertos a negociar la posibilidad una :violet[tercera propuesta].')