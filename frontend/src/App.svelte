<script>

  import axios from 'axios';

  let won;
  let waiting_for_response = false;

  const chooseMove = async (move) => {
    if(waiting_for_response)
      return;

    waiting_for_response = true;
    const response = await axios.post('/api/move/'+move);
    won = response.data.won;
    waiting_for_response = false;
  }

</script>

<main>

  <h1>shiv's rps</h1>
  <button on:click={() => chooseMove('rock')} class="move">🪨</button>
  <button on:click={() => chooseMove('paper')} class="move">📃</button>
  <button on:click={() => chooseMove('scissors')} class="move">✂</button>

  {#if won && !waiting_for_response}
    <h1>you won 🥇</h1>
  {:else if won != undefined && !waiting_for_response}
    <h1>you lost 😢</h1>
  {:else if won != undefined}
    <h1>waiting for bot's move...</h1>
  {/if}

</main>

<style>

  .move {
    font-size: 50px;
    border-radius: 20%;
  }

</style>