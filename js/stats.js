function stats(text) {
    const wordsPerMinute = 100; 

    // Count the words using any of the methods mentioned before
    const wordCount = text.split(/\s+/).filter(word => word !== "").length;

    // Calculate read time in minutes and round up to the nearest minute
    let readTimeMinutes = Math.ceil(wordCount / wordsPerMinute);

    // Format the output
    readTimeMinutes = readTimeMinutes === 1 ? "## 1" : `## ${readTimeMinutes}`;

    return [readTimeMinutes, '## ' + wordCount];
}