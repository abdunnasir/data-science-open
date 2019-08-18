<template>
<div id="app">
	<highcharts v-if="chartOptions" :options="chartOptions"></highcharts>
</div>
</template>

<script>
import axios from 'axios';
export default {
	name: 'app',
	data() {
		return {
			msg: 'Reality vs Prediction using vue high chart',
			chartOptions: null
		}
	},
	mounted() {
		axios
			.post("http://127.0.0.1:5000/")
			.then(response => {

				let realJson = response.data.real;
				let realData = [];
				realJson.forEach((item) => {
					realData.push(
                        [item.x, item.y]
					);
				});

				let predictedData = [];
				let predictedJson = response.data.predicted;
				predictedJson.forEach((item) => {
					predictedData.push(
                        [item.x, item.y]
					);
				});

				let graphData = [];
				graphData.push({
					name: 'Reality',
					data: realData,
					pointStart: 1
				});

				graphData.push({
					name: 'Prediction',
					data: predictedData,
					pointStart: 1
				});

				this.chartOptions = {
					series: graphData,
					title: {
						text: 'Reality vs Prediction using simple linear regression'
					},
				}
			});
	},

}
</script>

<style>
#app {
	font-family: 'Avenir', Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #2c3e50;
	margin-top: 60px;
}

h1,
h2 {
	font-weight: normal;
}

ul {
	list-style-type: none;
	padding: 0;
}

li {
	display: inline-block;
	margin: 0 10px;
}

a {
	color: #42b983;
}
</style>
