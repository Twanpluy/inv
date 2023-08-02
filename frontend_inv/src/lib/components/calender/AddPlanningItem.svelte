<script lang="ts">
	interface Categories {
		[key: string]: string;
	}

	let json_test_categories: Categories = { 1: 'Shift', 2: 'Event', 3: 'Deleveries', 4: 'Overige' };

	let selectedValue: string = '';
	function handleCategorySelection(event: Event) {
		const target = event.target as HTMLSelectElement;
		selectedValue = target.value;
	}

	export let dateId: string;

	export let dateHeading: string;
</script>

<section>
	<div id="modal" class="fixed inset-0 flex items-center justify-center bg-opacity-900">
		<div class="bg-white p-8 rounded-lg shadow-lg">
			<h1 class="text-2xl font-semibold mb-4">{dateHeading}</h1>

			<form method="post">
				<select class="select w-full max-w-xs" on:change={handleCategorySelection}>
					<option disabled selected>Pick category</option>
					{#each Object.keys(json_test_categories) as category}
						<option value={json_test_categories[category]}>
							{json_test_categories[category]}
						</option>
					{/each}
				</select>

				<div class="">
					<label class="label">
						<span class="label-text">Name</span>
					</label>
					<input type="text" placeholder="Item" class="input input-bordered" />
				</div>

				<!-- // if category is shift, show the time input -->
				{#if selectedValue.toLowerCase() === 'shift'}
					<div class="">
						<label class="label">
							<span class="label-text">Start Time</span>
						</label>
						<input type="time" placeholder="Time" class="input input-bordered" />

						<label class="label">
							<span class="label-text"> End Time</span>
						</label>
						<input type="time" placeholder="Time" class="input input-bordered" />
					</div>
				{/if}

				<label class="label">
					<span class="label-text">Date</span>
				</label>
				<input type="date" placeholder="Date" class="input input-bordered" />
				<p>{dateId}</p>
			</form>
			<div class="flex justify-end mt-4 py-4 py-4">
				<button class="btn-success px-4" on:click>Save</button>
				<button class="btn-error px-4" on:click>Close</button>
			</div>
		</div>
	</div>
</section>
