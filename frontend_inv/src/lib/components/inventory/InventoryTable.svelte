<script lang="ts">
	import AddOrder from './AddOrder.svelte';
	import jsonData from '/src/jsondata/inventory.json';
	// InventoryItem is the interface for the json data
	// Items have the following properties:
	// name, description, barcode, stock, prediction, deliverDate, brand, vendor, price
	interface InventoryItem {
		product_id: number;
		name: string;
		description: string;
		barcode: string;
		stock: number;
		prediction: number;
		deliverDate: string;
		brand: string;
		vendor: string;
		price: number;
	}

	let columns = [
		'name',
		'description',
		'stock',
		'prediction',
		'deliverDate',
		'brand',
		'vendor',
		'price',
		'order button',
		'delete button'
	];
	// Replace this data with your actual inventory data
	let inventory: InventoryItem[] = jsonData;

	function deleteItem(product_id: number) {
		inventory = inventory.filter((item) => item.product_id !== product_id);
	}

	//modal functionality
	let openmodal = false;

	function addToOrderList(product_id: number) {
		//modal to add to orderlist
		console.log(product_id);
		openmodal = true;
	}
</script>

<div class="overflow-x-auto">
	<div class="flex items-center justify-between mb-4">
		<!-- Search bar -->
		<input
			class="bg-gray-900 text-white px-4 py-3 rounded-md w-full"
			type="text"
			id="searchInput"
			placeholder="Search for items..."
		/>

		<!-- Search catorgy dropdown -->
		<button class="btn btn-primary px-4 py-2 ml-2">change to dropdown</button>

		<!-- Add Item button -->
		<button class="btn btn-success px-4 py-2 ml-2">Add Item</button>
	</div>

	<table class="table">
		<tr class="">
			{#each columns as column}
				<th class="bg-gray-800 font-bold text-white w-screen py-6 px-2">{column}</th>
			{/each}
		</tr>

		<!-- Get data -->
		{#each inventory as item}
			<tr class="border-b-2 border-gray-800 hover">
				{#each columns as column}
					{#if column === 'order button'}
						<td class="py-6 px-2">
							<button class="btn btn-info" on:click={() => addToOrderList(item.product_id)}
								>Add to orderlist</button
							>
						</td>
					{:else if column === 'delete button'}
						<td class="py-6 px-2">
							<button class="btn btn-error" on:click={() => deleteItem(item.product_id)}
								>Delete out of inventory</button
							>
						</td>
					{:else}
						<td class="py-6 px-2">{item[column]}</td>
					{/if}
				{/each}
			</tr>
		{/each}
	</table>
	<!-- // AddOrder is the modal component -->
	<AddOrder {openmodal} />
</div>
