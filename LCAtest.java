import static org.junit.Assert.assertEquals;
import org.junit.jupiter.api.Test;

class LCAtest {

	@Test
	void test() {
		LCA tree = new LCA();
		LCA tree1 = new LCA();

		tree.root = new Node(1);
		tree.root.left = new Node(2);
		tree.root.right = new Node(3);
		tree.root.left.left = new Node(4);
		tree.root.left.right = new Node(5);
		tree.root.right.left = new Node(6);
		tree.root.right.right = new Node(7);
		tree1.root = new Node(8);
		tree1.root = new Node(9);

		// testing LCA function returns correct result for regular node cases
		assertEquals("test", 2, tree.findLCA(4, 5));

		// tests if LCA returns 1 of the nodes searched
		assertEquals("test", 2, tree.findLCA(2, 4));

		// testing LCA function when result is root node
		assertEquals("test", 1, tree.findLCA(4, 6));

		// testing LCA when root node of 1 subtree & child node of 2nd subtree is parent
		// node
		assertEquals("test", 1, tree.findLCA(3, 4));

		// testing the case when the root node is the LCA
		assertEquals("test.", 1, tree.findLCA(1, 3));

	}

	@Test
	public void testNullTree() {
		LCA tree = new LCA();
		tree.root = null;
		assertEquals(-1, tree.findLCA(4, 5));
		// The output should be -1 since the tree is empty//
	}
}