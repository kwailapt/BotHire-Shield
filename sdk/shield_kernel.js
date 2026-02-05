/**
 * 🛡️ The Shield Protocol - Genesis Kernel (JS Edition)
 * Zero Dependency | Standardized Logic Primitives
 */

const ShieldKernel = {
    calculateTier: function(stake, tenureDays) {
        const power = BigInt(stake) * BigInt(tenureDays);
        if (power <= 0n) return 0;

        // Newton's Method for Integer Square Root (BigInt support)
        let x = power;
        let y = (x + 1n) / 2n;
        while (y < x) {
            x = y;
            y = (x + power / x) / 2n;
        }

        const score = Number(x);
        if (score < 100) return 1;  // Bronze
        if (score < 500) return 2;  // Silver
        if (score < 2000) return 3; // Gold
        return 4;                   // Diamond
    },

    verifyEnvelope: function(signature, payload, secret) {
        // Precise port of the Python ord() sum logic
        const combined = payload + secret;
        let sum = 0;
        for (let i = 0; i < combined.length; i++) {
            sum += combined.charCodeAt(i);
        }
        return signature === sum.toString();
    }
};

if (typeof module !== 'undefined') {
    module.exports = ShieldKernel;
}
