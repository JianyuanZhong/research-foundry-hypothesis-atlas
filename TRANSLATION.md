# Review languages and blinding

[← Expert review guide](REVIEW.md)

Chinese passages in 879 proposal documents and 52 catalog titles were translated into English on October 5, 2026. The process translated 7,699 distinct passages in parallel and reused repeated passages. Text outside the affected lines was retained, except for the removal of authoring metadata and the addition of a uniform review header.

That October 5 update changed language and blinding only. Its hypothesis IDs, parent links, dataset assignments, seed flags, and translated review copies remain preserved in the October 14 refresh.

The October 14 refresh adds frozen registered hypotheses from additional campaigns. Existing translations are reused for exact matching source passages. All catalog titles are in English. **339 newly added copies retain Chinese source passages**, including original source-column names, filenames, and some scientific prose. Their headers explicitly say **Anonymous source-language review copy**; the other proposals say **Anonymous English review copy**. Untranslated passages are retained as recorded rather than silently removed or represented as translated. This refresh performs no new model inference, research rollouts, or training.

## Blinded copies

Every proposal uses an anonymous review header identifying its language status. Individual review copies do not identify the producing model, provider, campaign, or translation provider. Individual provenance links are omitted. Source-to-review mappings, translation logs, and exact recorded originals are retained privately for audit.

Chinese source-field labels and descriptive strings are rendered in English for expert readability. These are display translations, not replacements for executable source-column names. Scientific citations and named methods are retained, including models used by cited studies; such references do not identify the hypothesis producer.

## Verification

The October 5 translation checks covered residual Chinese text, numeric values, links, Markdown structure, technical tokens, comparison signs, English negations, and explicit producer attribution. The October 14 refresh checks English catalog titles, accurate source-language notices, explicit producer attribution, complete proposal links, lineage, model attribution, and public redaction boundaries after rebuilding all trees and catalogs.

The translations are machine-assisted review copies. They do not constitute independent scientific validation. Review the current anonymous copies before consulting aggregate campaign information or repository history.
