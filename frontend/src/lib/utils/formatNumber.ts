// src/utils/formatNumber.js
export function formatNumber(num: number) {
	const thresholds = [
		{ value: 1e7, suffix: 'Cr' }, // 1 crore (10 million)
		{ value: 1e5, suffix: 'L' }, // 1 lakh (100,000)
		{ value: 1e3, suffix: 'k' } // 1 thousand (1,000)
	];

	for (const { value, suffix } of thresholds) {
		if (num >= value) {
			return (num / value).toFixed(1).replace(/\.0$/, '') + suffix;
		}
	}

	// Less than 1,000, show as is
	return num.toString();
}
