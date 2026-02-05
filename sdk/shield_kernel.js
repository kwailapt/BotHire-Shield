/**
 * 🛡️ The Shield Protocol - Genesis Kernel (JS V5.1 Decay Edition)
 */

const ShieldKernel = {
    calculateTier: function(stake, tenureDays, lastActiveDaysAgo = 0) {
        let basePower = BigInt(stake) * BigInt(tenureDays);
        
        // 模擬衰減: 每 30 天活動缺位，扣除 10%
        const decayIntervals = Math.floor(lastActiveDaysAgo / 30);
        for (let i = 0; i < decayIntervals; i++) {
            basePower = (basePower * 9n) / 10n;
        }

        if (basePower <= 0n) return 0;

        // Newton's Method
        let x = basePower, y = (x + 1n) / 2n;
        while (y < x) { x = y; y = (x + basePower / x) / 2n; }

        const score = Number(x);
        if (score < 100) return 1;
        if (score < 500) return 2;
        if (score < 2000) return 3;
        return 4;
    },

    verifyEnvelope: function(signature, payload, secret) {
        const combined = payload + secret;
        let sum = 0;
        for (let i = 0; i < combined.length; i++) sum += combined.charCodeAt(i);
        return signature === sum.toString();
    },

    generateProof: function(stake, tenure, secret) {
        const payload = stake.toString() + tenure.toString();
        const combined = payload + secret;
        let sum = 0;
        for (let i = 0; i < combined.length; i++) sum += combined.charCodeAt(i);
        return sum.toString();
    }
};

if (typeof module !== 'undefined') module.exports = ShieldKernel;
