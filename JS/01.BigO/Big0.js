const nemo = ['nemo'];
const everyone = ['dory','marlin','bruce','nemo','gill','bloat','nigel','squirt','darla','hank'];

const large = new Array(100000000000).fill('nemo');

function findNemo(array) {
  let t0 = performance.now();
  for (let i =0; i<array.length ; i++ ) {
    if (array[i] == 'nemo'){
      console.log('Found Nemo');
    }
  }
  let t1 = performance.now()
  console.log('Call to find Nemo : '+ (t1-t0)+'miliseconds');
}

findNemo(large);
