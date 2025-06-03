const { exec } = require('child_process')

exec('./run.sh', (err, stdout, stderr) => {
    if (err) {
        console.log(`stderr: ${stderr}`)
        return
    }
    console.log(`stdout: ${stdout}`)
})
console.log('a')
