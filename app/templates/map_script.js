	google.load('visualization', '1', {'packages': ['geochart']});
google.setOnLoadCallback(drawVisualization);

function escapeDiacritics(string)
{
	return string.replace(/ą/g, 'a').replace(/Ą/g, 'A')
		.replace(/ć/g, 'c').replace(/Ć/g, 'C')
		.replace(/ę/g, 'e').replace(/Ę/g, 'E')
		.replace(/ł/g, 'l').replace(/Ł/g, 'L')
		.replace(/ń/g, 'n').replace(/Ń/g, 'N')
		.replace(/ó/g, 'o').replace(/Ó/g, 'O')
		.replace(/ś/g, 's').replace(/Ś/g, 'S')
		.replace(/ż/g, 'z').replace(/Ż/g, 'Z')
		.replace(/ź/g, 'z').replace(/Ź/g, 'Z');
}

function drawVisualization() {

var myTable = [
	['State', 'Frekwencja'],
	['dolnośląskie', {{ attendance['dolnośląskie'] }}],
	['kujawsko-pomorskie', {{ attendance['kujawsko-pomorskie'] }}],
	['lubelskie', {{ attendance['lubelskie'] }}],
	['lubuskie', {{ attendance['lubuskie'] }}],
	['łódzkie', {{ attendance['łódzkie'] }}],
	['małopolskie', {{ attendance['małopolskie'] }}],
	['mazowieckie', {{ attendance['mazowieckie'] }}],
	['opolskie', {{ attendance['opolskie'] }}],
	['podkarpackie', {{ attendance['podkarpackie'] }}],
	['podlaskie', {{ attendance['podlaskie'] }}],
	['pomorskie', {{ attendance['pomorskie'] }}],
	['śląskie', {{ attendance['śląskie'] }}],
	['świętokrzyskie', {{ attendance['świętokrzyskie'] }}],
	['warmińsko-mazurskie', {{ attendance['warmińsko-mazurskie'] }}],
	['wielkopolskie', {{ attendance['wielkopolskie'] }}],
	['zachodniopomorskie', {{ attendance['zachodniopomorskie'] }}],
	]

var data = google.visualization.arrayToDataTable(myTable);

var opts = {
	region: 'PL',
	dataMode: 'regions',
	resolution: 'provinces',
	datalessRegionColor: 'transparent',
	defaultColor: '#CC1243',
	backgroundColor: 'transparent',
	width: 400,
	height: 300
	};

var geochart = new google.visualization.GeoChart(
		document.getElementById('visualization'));

function selectHandler(e) {
	 var selection = chart.getSelection();

	 alert('A table row was selected');
}

google.visualization.events.addListener(geochart, 'select', myClickHandler);

	function myClickHandler(e){
		var selection = geochart.getSelection();

		window.open(escapeDiacritics(
                'voivodeship/'
				+ myTable[selection[0].row + 1][0].toString())
				+ '.html', '_self'
			);
	}

geochart.draw(data, opts);
};
